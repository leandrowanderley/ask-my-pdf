# AskMyPDF

---

## 📚 Visão Geral do Projeto

O **AskMyPDF** é uma aplicação web interativa desenvolvida com **Django** que permite aos usuários fazer upload de arquivos PDF e, em seguida, fazer perguntas sobre o conteúdo desses documentos. Utilizando o poder do **Google Gemini API** e de modelos de linguagem e embeddings, o sistema extrai informações do PDF, as processa e gera respostas relevantes para as perguntas dos usuários.

---

## ✨ Funcionalidades

* **Upload de PDF:** Interface intuitiva para upload de arquivos PDF.
* **Extração de Texto:** Capacidade de extrair texto completo de documentos PDF.
* **Processamento de Texto:** Divide o conteúdo do PDF em "chunks" gerenciáveis para otimizar o processamento.
* **Criação de Vector Store:** Converte os chunks de texto em embeddings (vetores numéricos) e os armazena em um `vectorstore` (usando ChromaDB) para busca de similaridade semântica.
* **Geração de Respostas com IA:** Utiliza o modelo Gemini do Google para responder a perguntas baseadas no conteúdo do PDF, fornecendo respostas concisas e informativas.
* **Interface Amigável:** Frontend simples e responsivo para uma experiência de usuário agradável.
* **Estilização de Saída:** Suporte para renderização de estilizações de texto (negrito, itálico, listas, etc.) nas respostas, caso o Gemini as forneça.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:**
    * **Django:** Framework web Python para o desenvolvimento do servidor.
    * **Python:** Linguagem de programação principal.
    * **PyMuPDF (fitz):** Para extração de texto de PDFs.
    * **Langchain:** Framework para desenvolvimento de aplicações com Large Language Models (LLMs).
    * **Langchain-Google-GenAI:** Integração com o Google Gemini.
    * **HuggingFaceEmbeddings:** Para gerar embeddings de texto (usando o modelo `all-MiniLM-L6-v2`).
    * **ChromaDB:** Banco de dados vetorial para armazenar os embeddings.
    * **Python-Markdown:** Para converter Markdown em HTML no backend.
    * **python-dotenv:** Para gerenciamento de variáveis de ambiente.
* **Frontend:**
    * **HTML5:** Estrutura da página web.
    * **CSS3:** Estilização da interface.
    * **JavaScript:** Lógica de interação com o backend (requisições, exibição de respostas).

---

## 🚀 Como Configurar e Executar o Projeto Localmente

Siga estas instruções para configurar e executar o **AskMyPDF** em sua máquina local.

### Pré-requisitos

* **Python 3.10 ou superior**
* `pip` (gerenciador de pacotes do Python)
* Conexão com a internet para baixar modelos e acessar a API do Gemini.

### 1. Clonar o Repositório

Primeiro, clone o repositório para o seu ambiente local:

```bash
git clone [https://www.google.com/search?q=https://github.com/LeandroWanderley/AskMyPdf.git](https://www.google.com/search?q=https://github.com/LeandroWanderley/AskMyPdf.git)
cd AskMyPdf
```

c 2. Criar e Ativar o Ambiente Virtual
É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto.

```bash
python -m venv .venv
```

Ativar o ambiente virtual:

No macOS/Linux:
```Bash
source .venv/bin/activate
```
No Windows (Prompt de Comando):
```Bash
.venv\Scripts\activate
```
No Windows (PowerShell):
```PowerShell
.venv\Scripts\Activate.ps1
```

### 3. Instalar as Dependências
Crie um arquivo ```requirements.txt``` na raiz do seu projeto (`AskMyPdf/requirements.txt`) com o seguinte conteúdo:

```
Django
langchain
langchain-google-genai
langchain-community
langchain-huggingface
pymupdf # Instala fitz
markdown
python-dotenv
```
Após criar o arquivo, instale todas as dependências:

```Bash
pip install -r requirements.txt
```

### 4. Configurar a Chave da API do Gemini
Você precisará de uma chave da API do Google Gemini. Obtenha a sua em Google AI Studio.

Crie um arquivo chamado .env na raiz do seu projeto (AskMyPdf/.env) e adicione sua chave da API:

```
GEMINI_API_KEY="SUA_CHAVE_DA_API_DO_GEMINI_AQUI"
```
Lembre-se: O arquivo `.env` já está listado no `.gitignore` para garantir que sua chave não seja enviada para o controle de versão.

### 5. Executar as Migrações do Banco de Dados
Aplique as migrações iniciais do Django para configurar o banco de dados:

```Bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Iniciar o Servidor de Desenvolvimento
Agora você pode iniciar o servidor de desenvolvimento do Django:

```Bash
python manage.py runserver
```
Você verá uma mensagem indicando que o servidor está rodando, geralmente em `http://127.0.0.1:8000/`.

## 🌐 Utilização
Abra seu navegador web e navegue para `http://127.0.0.1:8000/`.
Você verá a interface do AskMyPDF.
Clique no botão "Escolher Arquivo" para fazer upload de um documento PDF.
No campo de texto, digite sua pergunta sobre o conteúdo do PDF.
Clique no botão "Perguntar ao PDF".
Aguarde enquanto o sistema processa o PDF e gera a resposta. A resposta aparecerá abaixo do formulário.

## 📂 Estrutura do Projeto
```
AskMyPdf/
├── .venv/                          # Ambiente virtual
├── AskMyPdf/                       # Diretório principal do projeto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                 # Configurações do projeto
│   ├── urls.py                     # URLs principais do projeto
│   └── wsgi.py
├── myapp/                          # Seu aplicativo Django
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py                    # Lógica das views (frontend e API)
│   ├── urls.py                     # URLs do aplicativo
│   ├── templates/                  # Templates HTML (myapp/index.html)
│   │   └── myapp/
│   │       └── index.html
│   └── static/                     # Arquivos estáticos (CSS, JS)
│       └── myapp/
│           └── script.js
│           └── style.css
│   └── src/                        # Módulos de lógica central
│       ├── __init__.py
│       ├── pdf_processor.py        # Extração de texto de PDF
│       ├── text_splitter.py        # Divisão de texto em chunks
│       ├── vectorstore.py          # Criação de vector store e embeddings
│       └── Youtubeer.py            # Lógica de perguntas e respostas com Gemini
├── manage.py                       # Utilitário de linha de comando do Django
├── requirements.txt                # Dependências do projeto
├── .env                            # Variáveis de ambiente (sua chave API)
├── .gitignore                      # Arquivos e diretórios a serem ignorados pelo Git
└── README.md                       # Este arquivo
```