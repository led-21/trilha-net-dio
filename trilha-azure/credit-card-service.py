import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

# Configurações do cliente
endpoint = "https://<seu-endpoint>.cognitiveservices.azure.com/"
key = "<sua-chave>"

document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

# Caminho para o documento de cartão de crédito
document_path = "caminho/para/seu/cartoes_de_creditos.pdf"

# Função para analisar o documento
def analyze_credit_card(document_path):
    with open(document_path, "rb") as document:
        poller = document_analysis_client.begin_analyze_document(
            "prebuilt-creditCard", document
        )
        result = poller.result()

    # Processar os resultados
    for page in result.pages:
        for table in page.tables:
            for cell in table.cells:
                print(f"Texto: {cell.content}, Confiança: {cell.confidence}")

# Analisar o documento
analyze_credit_card(document_path)
