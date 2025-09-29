// Define a URL do seu backend. Se estiver rodando localmente, será esta.
// Quando fizer o deploy, você precisará mudar para a URL da sua aplicação no Render.
const API_URL = 'http://127.0.0.1:8000'; 

// Seleciona os elementos do HTML
const emailText = document.getElementById('email-text');
const analyzeBtn = document.getElementById('analyze-btn');
const resultsSection = document.getElementById('results-section');
const categoryResult = document.getElementById('category-result');
const suggestionResult = document.getElementById('suggestion-result');
const loader = document.getElementById('loader');

// Adiciona o evento de clique ao botão
analyzeBtn.addEventListener('click', async () => {
    const text = emailText.value;

    // Validação simples
    if (!text.trim()) {
        alert('Por favor, insira o texto do e-mail.');
        return;
    }

    // Mostra o loader e esconde resultados antigos
    loader.classList.remove('hidden');
    resultsSection.classList.add('hidden');
    analyzeBtn.disabled = true;

    try {
        // Faz a requisição para a API
        const response = await fetch(`${API_URL}/analyze-email/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text }),
        });

        if (!response.ok) {
            throw new Error('A resposta da rede não foi bem-sucedida.');
        }

        const data = await response.json();

        // Exibe os resultados
        categoryResult.textContent = data.category || 'N/A';
        suggestionResult.textContent = data.suggestion || 'N/A';
        resultsSection.classList.remove('hidden');

    } catch (error) {
        console.error('Erro ao analisar o e-mail:', error);
        alert('Ocorreu um erro ao processar sua solicitação. Tente novamente.');
    } finally {
        // Esconde o loader e reativa o botão
        loader.classList.add('hidden');
        analyzeBtn.disabled = false;
    }
});