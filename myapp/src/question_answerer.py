# question_answerer.py
from langchain.prompts import PromptTemplate
from langchain_core.runnables import chain, RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
import markdown # Importa a biblioteca markdown para converter Markdown em HTML

def configure_genai(api_key, model_name="gemini-1.5-flash"):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(
        model_name=model_name,
        generation_config={
            "temperature": 0.8,
            "top_p": 0.9,
            "top_k": 50,
            "max_output_tokens": 4000,
            # Removido "response_mime_type": "text/plain",
            # Isso permite que o Gemini retorne Markdown ou outros formatos,
            # que será então convertido para HTML.
        }
    )

def answer_question(vectorstore, question, gemini_api_key):
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7, google_api_key=gemini_api_key)

    template = """Contexto:
    {context}

    Pergunta:
    {question}

    Por favor, formate sua resposta usando Markdown para negrito, itálico, listas, etc.
    """ # Adicionei uma instrução ao prompt para encorajar o Gemini a usar Markdown
    prompt = PromptTemplate.from_template(template)

    retrieval_chain = (
        {"context": vectorstore.as_retriever(search_kwargs={"k": 4}), "question": RunnablePassthrough()}
        | prompt
        | model
    )

    response = retrieval_chain.invoke(question)
    
    # Converte o conteúdo da resposta de Markdown para HTML
    html_response = markdown.markdown(response.content)
    return html_response # Retorna o HTML formatado

if __name__ == '__main__':
    print("Sim")
