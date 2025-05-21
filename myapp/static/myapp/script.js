// script.js

// Obtém referências aos elementos do DOM
const form = document.getElementById('askPdfForm');
const pdfFileInput = document.getElementById('pdfFile');
const questionInput = document.getElementById('question');
const loadingIndicator = document.getElementById('loadingIndicator');
const responseContainer = document.getElementById('responseContainer');
const answerText = document.getElementById('answerText');
const errorContainer = document.getElementById('errorContainer');
const errorText = document.getElementById('errorText');

// Adiciona um listener para o evento de submit do formulário
form.addEventListener('submit', async (event) => {
    event.preventDefault(); // Previne o comportamento padrão de submit do formulário (recarregar a página)

    // Esconde a resposta e o erro anteriores, mostra o indicador de carregamento
    responseContainer.classList.add('hidden');
    errorContainer.classList.add('hidden');
    loadingIndicator.classList.remove('hidden');

    const formData = new FormData(); // Cria um objeto FormData para enviar o arquivo e a pergunta
    formData.append('pdfFile', pdfFileInput.files[0]); // Adiciona o arquivo PDF
    formData.append('question', questionInput.value); // Adiciona a pergunta

    try {
        // Faz uma requisição POST para o endpoint do Django (substitua '/api/ask-pdf/' pelo seu URL real)
        const response = await fetch('/api/ask-pdf/', {
            method: 'POST',
            body: formData, // Envia o FormData
            // Headers como 'Content-Type': 'multipart/form-data' são automaticamente definidos pelo navegador ao usar FormData
        });

        // Verifica se a resposta da requisição foi bem-sucedida
        if (!response.ok) {
            const errorData = await response.json(); // Tenta ler o JSON de erro
            throw new Error(errorData.error || 'Ocorreu um erro ao processar sua solicitação.');
        }

        const data = await response.json(); // Analisa a resposta JSON
        // Altera de textContent para innerHTML para renderizar estilizações HTML
        answerText.innerHTML = data.answer; // Define o texto da resposta
        responseContainer.classList.remove('hidden'); // Mostra o contêiner da resposta

    } catch (error) {
        console.error('Erro na requisição:', error);
        errorText.textContent = error.message; // Exibe a mensagem de erro
        errorContainer.classList.remove('hidden'); // Mostra o contêiner de erro
    } finally {
        loadingIndicator.classList.add('hidden'); // Esconde o indicador de carregamento
    }
});
