# AskMyPDF

---

## 📚 Project Overview

**AskMyPDF** is an interactive web application built with **Django** that allows users to upload PDF files and then ask questions about the content of those documents. Using the power of the **Google Gemini API** and language models and embeddings, the system extracts information from the PDF, processes it, and generates relevant answers to the user's questions.

---

## ✨ Features

* **PDF Upload:** Intuitive interface for uploading PDF files.
* **Text Extraction:** Ability to extract full text from PDF documents.
* **Text Processing:** Breaks PDF content into manageable chunks for faster processing. * **Vector Store Creation:** Converts text chunks into embeddings (numeric vectors) and stores them in a `vectorstore` (using ChromaDB) for semantic similarity searching.
* **AI-Powered Answer Generation:** Uses Google's Gemini model to answer questions based on the PDF content, providing concise and informative answers.
* **User-Friendly Interface:** Simple and responsive frontend for a pleasant user experience.
* **Output Styling:** Support for rendering text styling (bold, italic, lists, etc.) in the answers, if Gemini provides them.

---

## 🛠️ Technologies Used

* **Backend:**
* **Django:** Python web framework for server development.
* **Python:** Main programming language.
* **PyMuPDF (fitz):** For extracting text from PDFs.
* **Langchain:** Framework for developing applications with Large Language Models (LLMs).
* **Langchain-Google-GenAI:** Integration with Google Gemini.
* **HuggingFaceEmbeddings:** For generating text embeddings (using the `all-MiniLM-L6-v2` model).
* **ChromaDB:** Vector database for storing the embeddings.
* **Python-Markdown:** For converting Markdown to HTML in the backend.
* **python-dotenv:** For managing environment variables.
* **Frontend:**
* **HTML5:** Structure of the web page.
* **CSS3:** Styling of the interface.
* **JavaScript:** Logic for interacting with the backend (requests, displaying responses).

---

## 🚀 How to Set Up and Run the Project Locally

Follow these instructions to set up and run **AskMyPDF** on your local machine.

### Prerequisites

* **Python 3.10 or higher**
* `pip` (Python package manager)
* Internet connection to download models and access the Gemini API.

### 1. Clone the Repository

First, clone the repository to your local environment:

```bash
git clone [https://www.google.com/search?q=https://github.com/LeandroWanderley/AskMyPdf.git](https://www.google.com/search?q=https://github.com/LeandroWanderley/AskMyPdf.git)
cd AskMyPdf
```

c 2. Create and Activate the Virtual Environment
It is highly recommended to use a virtual environment to isolate project dependencies.

```bash
python -m venv .venv
```

Activate the virtual environment:

On macOS/Linux:
```Bash
source .venv/bin/activate
```
On Windows (Command Prompt):
```Bash
.venv\Scripts\activate
```
On Windows (PowerShell):
```PowerShell
.venv\Scripts\Activate.ps1
```

### 3. Install the Dependencies
Create a ```requirements.txt``` file in the root of your project (`AskMyPdf/requirements.txt`) with the following content:

```
Django
langchain
langchain-google-genai
langchain-community
langchain-huggingface
pymupdf # Install fitz
markdown
python-dotenv
```
After creating the file, install all dependencies:

```Bash
pip install -r requirements.txt
```

### 4. Set up the Gemini API Key
You will need a Google Gemini API key. Get yours from Google AI Studio.

Create a file called .env in the root of your project (AskMyPdf/.env) and add your API key:

```
GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
```
Remember: The `.env` file is already listed in `.gitignore` to ensure that your key is not committed to version control.

### 5. Run the Database Migrations
Apply the initial Django migrations to set up the database:

```Bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the Development Server
Now you can start the Django development server:

```Bash
python manage.py runserver
```
You will see a message indicating that the server is running, usually at `http://127.0.0.1:8000/`.

## 🌐 Usage
Open your web browser and navigate to `http://127.0.0.1:8000/`.
You will see the AskMyPDF interface.
Click the "Choose File" button to upload a PDF document.
In the text field, type your question about the contents of the PDF.
Click the "Ask PDF Question" button.
Please wait while the system processes the PDF and generates the response. The response will appear below the form.

## 📂 Project Structure
```
AskMyPdf/
├── .venv/                      # Virtual environment
├── AskMyPdf/                   # Main Django project directory
│ ├── __init__.py
│ ├── asgi.py
│ ├── settings.py               # Project settings
│ ├── urls.py                   # Main project URLs
│ └── wsgi.py
├── myapp/                      # Your Django application
│ ├── migrations/
│ ├── __init__.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── views.py                  # View logic (frontend and API)
│ ├── urls.py                   # Application URLs
│ ├── templates/                # HTML templates (myapp/index.html)
│ │ └── myapp/
│ │ └── index.html
│ └── static/                   # Static files (CSS, JS)
│ └── myapp/
│ └── script.js
│ └── style.css
│ └── src/                      # Core logic modules
│ ├── __init__.py
│ ├── pdf_processor.py          # Extracting text from PDF
│ ├── text_splitter.py          # Splitting text into chunks
│ ├── vectorstore.py            # Creating vector store and embeddings
│ └── Youtubeer.py              # Q&A logic with Gemini
├── manage.py                   # Django command-line utility
├── requirements.txt            # Project dependencies
├── .env                        # Environment variables (your API key)
├── .gitignore                  # Files and directories to be ignored by Git
└── README.md                   # This file
```