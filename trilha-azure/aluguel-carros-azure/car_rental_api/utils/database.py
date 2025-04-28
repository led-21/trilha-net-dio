import pyodbc
import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def get_db_connection():
    credential = DefaultAzureCredential()
    key_vault_url = os.getenv("AZURE_KEY_VAULT_URL")
    
    # Busca a connection string no Azure Key Vault
    secret_client = SecretClient(vault_url=key_vault_url, credential=credential)
    conn_str = secret_client.get_secret("SQL-CONNECTION-STRING").value
    
    return pyodbc.connect(conn_str)
