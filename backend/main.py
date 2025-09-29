import os
import fitz # Importa o PyMuPDF
from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o cliente da OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Inicializa a aplicação FastAPI
app = FastAPI()

# Configuração do CORS
origins = ["*"] # Simplificado para aceitar todas as origens

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint de "health check"
@app.get("/")
def read_root():
    return {"status": "API is running"}

# --- NOSSO ENDPOINT MODIFICADO ---
@app.post("/analyze-email/")
async def analyze_email(text: Optional[str] = Form(None), file: Optional[UploadFile] = File(None)):
    email_text = ""

    if not text and not file:
        return {"error": "Nenhum texto ou arquivo foi enviado."}

    if file:
        # Lê o conteúdo do arquivo
        contents = await file.read()
        
        # Se for um arquivo PDF
        if file.content_type == 'application/pdf':
            try:
                # Usa o PyMuPDF para abrir o PDF a partir dos bytes
                with fitz.open(stream=contents, filetype="pdf") as doc:
                    for page in doc:
                        email_text += page.get_text()
            except Exception as e:
                return {"error": f"Erro ao processar o arquivo PDF: {str(e)}"}
        # Se for um arquivo de texto
        elif file.content_type == 'text/plain':
            email_text = contents.decode('utf-8')
        else:
            return {"error": "Formato de arquivo não suportado. Use .txt ou .pdf."}

    elif text:
        email_text = text

    if not email_text.strip():
        return {"error": "O conteúdo do e-mail está vazio."}
        
    try:
        # Passo 1: Classificar o email (a lógica da IA continua a mesma)
        classification_prompt = f"""
        Analise o seguinte texto de um e-mail e classifique-o como 'Produtivo' ou 'Improdutivo'.
        - 'Produtivo': E-mails que requerem uma ação, resposta específica, contêm solicitações, dúvidas ou atualizações sobre trabalho.
        - 'Improdutivo': E-mails que são apenas cumprimentos, agradecimentos, felicitações ou não relacionados a uma tarefa.

        E-mail: "{email_text}"
        
        Classificação:
        """
        
        response_classification = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": classification_prompt}],
            max_tokens=10,
            temperature=0.0
        )
        category = response_classification.choices[0].message.content.strip()

        # Passo 2: Gerar uma resposta sugerida
        suggestion_prompt = f"""
        Com base na categoria '{category}' e no conteúdo do e-mail abaixo, gere uma resposta curta e profissional.
        - Se for 'Produtivo', a resposta deve acusar o recebimento e informar que a solicitação está sendo tratada.
        - Se for 'Improdutivo', a resposta deve ser um agradecimento simples e cordial.

        E-mail: "{email_text}"

        Resposta Sugerida:
        """

        response_suggestion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": suggestion_prompt}],
            max_tokens=100,
            temperature=0.7
        )
        suggestion = response_suggestion.choices[0].message.content.strip()

        return {"category": category, "suggestion": suggestion}

    except Exception as e:
        return {"error": str(e)}