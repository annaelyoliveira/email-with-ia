// A URL da API deve estar configurada para a do Render
const API_URL = 'https://email-with-ia.onrender.com'; // <-- CONFIRME SE ESTA É SUA URL CORRETA

// Seleciona os elementos do HTML
const emailText = document.getElementById('email-text');
const analyzeBtn = document.getElementById('analyze-btn');
const resultsSection = document.getElementById('results-section');
const categoryResult = document.getElementById('category-result');
const suggestionResult = document.getElementById('suggestion-result');
const loader = document.getElementById('loader');
const fileUpload = document.getElementById('file-upload');
const fileNameSpan = document.getElementById('file-name');
const errorBox = document.getElementById('error-box');
const errorResult = document.getElementById('error-result');

// Mostra o nome do arquivo selecionado
fileUpload.addEventListener('change', () => {
    if (fileUpload.files.length > 0) {
        fileNameSpan.textContent = fileUpload.files[0].name;
        emailText.value = ''; // Limpa o textarea se um arquivo for selecionado
    } else {
        fileNameSpan.textContent = 'Nenhum arquivo selecionado';
    }
});

// Limpa a seleção de arquivo se o usuário digitar no textarea
emailText.addEventListener('input', () => {
    if (emailText.value.trim() !== '') {
        fileUpload.value = ''; // Reseta o input de arquivo
        fileNameSpan.textContent = 'Nenhum arquivo selecionado';
    }
});


// Adiciona o evento de clique ao botão
analyzeBtn.addEventListener('click', async () => {
    const text = emailText.value;
    const file = fileUpload.files[0];

    // Validação
    if (!text.trim() && !file) {
        alert('Por favor, insira um texto ou selecione um arquivo.');
        return;
    }

    // Prepara os dados para envio
    const formData = new FormData();
    if (file) {
        formData.append('file', file);
    } else {
        formData.append('text', text);
    }
    
    // Mostra o loader e esconde resultados antigos
    loader.classList.remove('hidden');
    resultsSection.classList.add('hidden');
    errorBox.classList.add('hidden');
    analyzeBtn.disabled = true;

    try {
        // Faz a requisição para a API
        const response = await fetch(`${API_URL}/analyze-email/`, {
            method: 'POST',
            body: formData, // Envia como FormData, não JSON
            // NÃO definimos o 'Content-Type', o navegador faz isso automaticamente para FormData
        });

        const data = await response.json();

        if (!response.ok || data.error) {
            throw new Error(data.error || 'A resposta da rede não foi bem-sucedida.');
        }

        // Exibe os resultados
        categoryResult.textContent = data.category || 'N/A';
        suggestionResult.textContent = data.suggestion || 'N/A';
        resultsSection.classList.remove('hidden');

    } catch (error) {
        console.error('Erro ao analisar o e-mail:', error);
        errorResult.textContent = error.message;
        errorBox.classList.remove('hidden');
    } finally {
        // Esconde o loader e reativa o botão
        loader.classList.add('hidden');
        analyzeBtn.disabled = false;
    }
});