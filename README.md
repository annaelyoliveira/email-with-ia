# Analisador de E-mails com IA 🚀


<img width="1916" height="904" alt="Captura de tela 2025-09-29 154211" src="https://github.com/user-attachments/assets/50e8577c-2935-461f-916e-bb0af80a5ff5" />

## 📝 Descrição do Projeto

Este projeto foi desenvolvido como solução para o **Case Prático do processo seletivo da AutoU**. O objetivo é otimizar a rotina de uma equipe que lida com um alto volume de e-mails, automatizando a leitura, classificação e a sugestão de respostas.

A aplicação utiliza Inteligência Artificial para analisar o conteúdo de um e-mail (seja por texto direto ou upload de arquivos `.txt` e `.pdf`) e o classifica em duas categorias principais: **Produtivo** ou **Improdutivo**, sugerindo uma resposta adequada para cada caso e liberando tempo da equipe para tarefas de maior valor.

---

## 🚀 Aplicação Online

A aplicação está publicada e pode ser acessada através do link abaixo. A primeira requisição pode demorar um pouco mais (cerca de 30s) para "acordar" o servidor gratuito do Render.

**[https://joyful-bubblegum-06dc2c.netlify.app/](https://joyful-bubblegum-06dc2c.netlify.app/)**

---

## ✨ Funcionalidades Principais

* **Análise de E-mail via Texto:** Permite colar o conteúdo de um e-mail diretamente na interface.
* **Upload de Arquivos:** Suporte para upload de arquivos nos formatos `.txt` e `.pdf` para análise.
* **Classificação com IA:** Utiliza a API da OpenAI para categorizar os e-mails em:
    * **Produtivo:** Requer uma ação ou resposta específica.
    * **Improdutivo:** Não necessita de uma ação imediata (agradecimentos, felicitações, etc.).
* **Sugestão de Resposta:** Gera uma resposta automática e contextualizada com base na classificação.
* **Interface Fluida e Moderna:** Design focado na experiência do usuário (UI/UX), com um visual profissional e agradável.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído com uma arquitetura desacoplada, utilizando tecnologias modernas para cada parte da aplicação:

* **Backend:**
    * **Python 3**
    * **FastAPI:** Para a construção da API de alta performance.
    * **Uvicorn:** Como servidor ASGI.
    * **PyMuPDF:** Para a extração de texto de arquivos PDF.

* **Frontend:**
    * **HTML5**
    * **CSS3**
    * **JavaScript (Vanilla JS):** Para a lógica da interface e comunicação com a API.

* **Inteligência Artificial:**
    * **OpenAI API (GPT-3.5 Turbo):** Para os processos de classificação e geração de texto.

* **Hospedagem (Deploy):**
    * **Render:** Para a hospedagem do backend.
    * **Netlify:** Para a hospedagem do frontend.
    * **Git & GitHub:** Para versionamento de código e Continuous Deployment (CI/CD).

---

## ⚙️ Como Executar o Projeto Localmente

Siga os passos abaixo para rodar a aplicação no seu ambiente de desenvolvimento.

**Pré-requisitos:**
* [Python 3.9+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)
* Um editor de código como o [VS Code](https://code.visualstudio.com/)

**Instalação:**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/annaelyoliveira/email-with-ia.git](https://github.com/annaelyoliveira/email-with-ia.git)
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd email-with-ia
    ```

3.  **Configure e ative o ambiente virtual para o backend:**
    ```bash
    # Navegue para a pasta do backend
    cd backend

    # Crie o ambiente virtual
    python -m venv venv

    # Ative o ambiente virtual
    # No Windows:
    venv\Scripts\activate
    # No Mac/Linux:
    source venv/bin/activate
    ```

4.  **Instale as dependências do backend:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure as variáveis de ambiente:**
    * Ainda na pasta `backend/`, crie um arquivo chamado `.env`.
    * Dentro deste arquivo, adicione sua chave da OpenAI:
        ```
        OPENAI_API_KEY="sk-sua-chave-aqui"
        ```

**Executando a Aplicação:**

1.  **Inicie o servidor backend:**
    (Ainda no terminal, dentro da pasta `backend/` com o `venv` ativado)
    ```bash
    uvicorn main:app --reload
    ```
    O servidor estará rodando em `http://127.0.0.1:8000`.

2.  **Inicie o frontend:**
    * Abra o projeto no VS Code.
    * Instale a extensão [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer).
    * Clique com o botão direito no arquivo `frontend/index.html` e selecione "Open with Live Server".
    * O site abrirá no seu navegador em um endereço como `http://127.0.0.1:5500`.

---

## 🔑 Autenticação

A aplicação **não requer login ou autenticação** para ser utilizada, conforme o escopo do desafio. A interface é de acesso direto.

---

## 👤 Autor

**Annaely Oliveira**

* [LinkedIn](https://www.linkedin.com/in/annaelyoliveira/)
* [GitHub](https://github.com/annaelyoliveira)
