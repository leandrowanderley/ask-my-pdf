# myapp/views.py

import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Importe suas funções existentes do diretório 'src'.
# Certifique-se de que a pasta 'src' está dentro do seu aplicativo Django ('myapp').
# Ex: myproject/myapp/src/pdf_processor.py
from myapp.src.pdf_processor import extract_text_from_pdf
from myapp.src.text_splitter import split_text
from myapp.src.vectorstore import create_vectorstore
from myapp.src.question_answerer import answer_question

# View para servir o arquivo HTML do frontend
def index(request):
    """
    View para renderizar o template HTML principal do aplicativo.
    """
    return render(request, 'myapp/index.html')

@csrf_exempt # Desabilita a proteção CSRF para este endpoint. Use com cuidado em produção!
             # Para produção, considere usar autenticação baseada em token ou outras estratégias de segurança.
def ask_pdf_view(request):
    """
    View do Django para processar o upload de PDF e a pergunta do usuário.
    Recebe um arquivo PDF e uma pergunta via POST, processa-os e retorna uma resposta JSON.
    """
    if request.method == 'POST':
        # Verifica se o arquivo PDF e a pergunta foram enviados na requisição
        if 'pdfFile' not in request.FILES or 'question' not in request.POST:
            return JsonResponse({'error': 'Arquivo PDF e/ou pergunta ausentes.'}, status=400)

        pdf_file = request.FILES['pdfFile']
        question = request.POST['question']

        # Obtém a chave da API do Gemini das configurações do Django.
        # É altamente recomendado configurar GEMINI_API_KEY como uma variável de ambiente.
        gemini_api_key = os.getenv('GEMINI_API_KEY', '') # Tenta obter da variável de ambiente
        if not gemini_api_key:
            # Se não encontrada na variável de ambiente, tenta do settings.py (menos seguro para produção)
            gemini_api_key = getattr(settings, 'GEMINI_API_KEY', '')

        if not gemini_api_key:
            return JsonResponse({'error': 'Erro: Chave da API do Gemini não configurada. Por favor, defina a variável de ambiente GEMINI_API_KEY ou no settings.py.'}, status=500)

        # Configura o sistema de armazenamento de arquivos para salvar temporariamente o PDF
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        filename = fs.save(pdf_file.name, pdf_file)
        temp_pdf_path = fs.path(filename) # Caminho completo para o arquivo salvo

        try:
            # Extrai o texto do PDF usando sua função existente
            text = extract_text_from_pdf(temp_pdf_path)
            if "Erro:" in text:
                return JsonResponse({'error': text}, status=400)

            # Divide o texto em chunks
            chunks = split_text(text)

            # Cria o vectorstore
            vectorstore = create_vectorstore(chunks)

            # Responde à pergunta
            answer = answer_question(vectorstore, question, gemini_api_key)

            return JsonResponse({'answer': answer})

        except Exception as e:
            # Captura e retorna erros inesperados durante o processamento
            return JsonResponse({'error': f'Ocorreu um erro interno: {str(e)}'}, status=500)
        finally:
            # Garante que o arquivo PDF temporário seja removido, mesmo em caso de erro
            if os.path.exists(temp_pdf_path):
                os.remove(temp_pdf_path)
    else:
        # Retorna erro se o método da requisição não for POST
        return JsonResponse({'error': 'Método não permitido. Use POST.'}, status=405)

