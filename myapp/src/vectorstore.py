from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do ficheiro .env

def create_vectorstore(chunks):
    """
    Cria um vectorstore a partir dos chunks de texto usando Chroma e HuggingFaceEmbeddings.

    Args:
        chunks (list): Uma lista de objetos Document contendo os chunks de texto.

    Returns:
        Chroma: Um objeto Chroma representando o vectorstore.
    """
    # Inicializa o modelo de embedding do Hugging Face.
    # O argumento 'device="cpu"' foi removido, pois não é mais aceito nesta versão da biblioteca.
    # A biblioteca deve inferir o dispositivo correto (CPU) por padrão.
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Cria o vectorstore Chroma a partir dos chunks e embeddings
    vectorstore = Chroma.from_documents(documents=chunks, embedding=embedding)
    return vectorstore

if __name__ == '__main__':
    # Cria alguns chunks de exemplo para teste
    from langchain.docstore.document import Document
    chunks_de_exemplo = [
        Document(page_content="Este é o primeiro chunk.", metadata={"nome do arquivo": "exemplo.pdf"}),
        Document(page_content="Este é o segundo chunk, que é um pouco mais longo.", metadata={"nome do arquivo": "exemplo.pdf"}),
        Document(page_content="Este é o terceiro e último chunk.", metadata={"nome do arquivo": "exemplo.pdf"})
    ]
    # Chama a função para criar o vectorstore
    vectorstore_criado = create_vectorstore(chunks_de_exemplo)
    # Imprime informações sobre o vectorstore criado (para depuração)
    print(f"Vectorstore criado: {vectorstore_criado}")
