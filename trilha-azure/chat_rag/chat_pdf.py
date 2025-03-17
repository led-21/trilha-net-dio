import os
import PyPDF2
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from flask import Flask, request, jsonify

# Configuração da API da OpenAI (substitua pela sua chave)
os.environ["OPENAI_API_KEY"] = "sua-chave-openai-aqui"

# Função para extrair texto de PDFs
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Função para processar o texto e criar embeddings
def process_text_and_create_embeddings(texts):
    # Dividir o texto em chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(texts)

    # Gerar embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  # Alternativa: OpenAIEmbeddings()
    vector_store = FAISS.from_texts(chunks, embeddings)
    return vector_store

# Função para criar o sistema de QA
def create_qa_system(vector_store):
    llm = OpenAI(temperature=0)  # Modelo GPT da OpenAI
    qa_system = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever()
    )
    return qa_system

# Interface de chat usando Flask
app = Flask(__name__)

# Rota para carregar PDFs e processar o texto
@app.route("/load_pdf", methods=["POST"])
def load_pdf():
    if "file" not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400
    
    file = request.files["file"]
    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(file)
        global qa_system
        vector_store = process_text_and_create_embeddings(text)
        qa_system = create_qa_system(vector_store)
        return jsonify({"message": "PDF carregado e processado com sucesso!"}), 200
    else:
        return jsonify({"error": "Formato de arquivo inválido"}), 400

# Rota para fazer perguntas
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    if "question" not in data:
        return jsonify({"error": "Pergunta não fornecida"}), 400
    
    question = data["question"]
    if not qa_system:
        return jsonify({"error": "Nenhum PDF foi carregado ainda"}), 400
    
    answer = qa_system.run(question)
    return jsonify({"question": question, "answer": answer}), 200

# Iniciar o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)
