import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware # Importe o CORS

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o cliente da OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Inicializa a aplicação FastAPI
app = FastAPI()

# --- Configuração do CORS ---
# Permite que o frontend (que estará em uma origem diferente)
# se comunique com este backend.
origins = [
    "http://localhost:5500",  # Endereço do Live Server do VSCode
    "http://127.0.0.1:5500", # Outra variação do localhost
    "*" # Em produção, seja mais específico. Para o desafio, "*" é aceitável.
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -----------------------------

# Define o formato de dados que a API espera receber
class EmailRequest(BaseModel):
    text: str

# Define o endpoint principal da API
@app.post("/analyze-email/")
async def analyze_email(request: EmailRequest):
    email_text = request.text

    try:
        # Passo 1: Classificar o email
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

# Endpoint de "health check" para verificar se a API está no ar
@app.get("/")
def read_root():
    return {"status": "API is running"}