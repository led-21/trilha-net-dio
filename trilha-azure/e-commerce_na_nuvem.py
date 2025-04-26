from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, PublicAccess
from azure.identity import DefaultAzureCredential
import os
import json
from datetime import datetime
import uuid
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EcommerceBlobStorage:
    def __init__(self, account_url, container_name):
        """
        Inicializa o cliente do Azure Blob Storage
        
        Args:
            account_url (str): URL da conta de armazenamento (ex: "https://<account_name>.blob.core.windows.net")
            container_name (str): Nome do container principal
        """
        self.account_url = account_url
        self.container_name = container_name
        
        # Usando DefaultAzureCredential para autenticação segura
        self.credential = DefaultAzureCredential()
        
        # Cria o BlobServiceClient
        self.blob_service_client = BlobServiceClient(
            account_url=self.account_url, 
            credential=self.credential
        )
        
        # Garante que o container existe
        self.container_client = self._get_or_create_container(container_name)
        
        # Dicionário para mapeamento de tipos de dados
        self.data_types = {
            'product': 'products',
            'order': 'orders',
            'customer': 'customers',
            'image': 'images',
            'inventory': 'inventory',
            'review': 'reviews'
        }

    def _get_or_create_container(self, container_name):
        """Cria o container se não existir"""
        try:
            container_client = self.blob_service_client.get_container_client(container_name)
            if not container_client.exists():
                container_client.create_container()
                logger.info(f"Container {container_name} criado com sucesso.")
            return container_client
        except Exception as e:
            logger.error(f"Erro ao acessar/criar container: {str(e)}")
            raise

    def _get_blob_path(self, data_type, identifier=None, file_extension=None):
        """
        Gera um caminho estruturado para o blob
        
        Args:
            data_type (str): Tipo de dado (product, order, customer, etc.)
            identifier (str): ID único do item (opcional)
            file_extension (str): Extensão do arquivo (opcional)
            
        Returns:
            str: Caminho completo para o blob
        """
        if data_type not in self.data_types:
            raise ValueError(f"Tipo de dado inválido. Opções válidas: {list(self.data_types.keys())}")
            
        folder = self.data_types[data_type]
        date_part = datetime.now().strftime("%Y/%m/%d")
        
        if not identifier:
            identifier = str(uuid.uuid4())
            
        if file_extension:
            return f"{folder}/{date_part}/{identifier}.{file_extension}"
        return f"{folder}/{date_part}/{identifier}.json"

    def upload_data(self, data, data_type, identifier=None, metadata=None):
        """
        Faz upload de dados para o Blob Storage
        
        Args:
            data: Dados a serem armazenados (dict ou bytes)
            data_type (str): Tipo de dado (product, order, customer, etc.)
            identifier (str): ID único do item (opcional)
            metadata (dict): Metadados adicionais (opcional)
            
        Returns:
            str: ID do blob criado
        """
        try:
            if isinstance(data, dict):
                blob_data = json.dumps(data).encode('utf-8')
                file_extension = 'json'
            elif isinstance(data, bytes):
                blob_data = data
                file_extension = None  # Será determinado pelo nome do arquivo
            else:
                raise ValueError("Tipo de dado não suportado. Use dict ou bytes.")
            
            blob_path = self._get_blob_path(data_type, identifier, file_extension)
            blob_client = self.container_client.get_blob_client(blob_path)
            
            # Configura metadados padrão
            default_metadata = {
                'upload_time': datetime.utcnow().isoformat(),
                'data_type': data_type,
                'source': 'e-commerce-platform'
            }
            
            if metadata:
                default_metadata.update(metadata)
            
            blob_client.upload_blob(
                data=blob_data,
                metadata=default_metadata,
                overwrite=True
            )
            
            logger.info(f"Dados do tipo {data_type} armazenados em {blob_path}")
            return blob_path
        except Exception as e:
            logger.error(f"Erro ao fazer upload de dados: {str(e)}")
            raise

    def download_data(self, blob_path):
        """
        Baixa dados do Blob Storage
        
        Args:
            blob_path (str): Caminho completo do blob
            
        Returns:
            dict or bytes: Dados armazenados
        """
        try:
            blob_client = self.container_client.get_blob_client(blob_path)
            blob_data = blob_client.download_blob().readall()
            
            # Verifica se é JSON
            if blob_path.endswith('.json'):
                return json.loads(blob_data.decode('utf-8'))
            return blob_data
        except Exception as e:
            logger.error(f"Erro ao baixar dados: {str(e)}")
            raise

    def list_data(self, data_type=None, date_prefix=None):
        """
        Lista blobs no container
        
        Args:
            data_type (str): Tipo de dado para filtrar (opcional)
            date_prefix (str): Prefixo de data no formato YYYY/MM/DD (opcional)
            
        Returns:
            list: Lista de blobs encontrados
        """
        try:
            prefix = ""
            if data_type and data_type in self.data_types:
                prefix = f"{self.data_types[data_type]}/"
                if date_prefix:
                    prefix += f"{date_prefix}/"
            
            blobs = self.container_client.list_blobs(name_starts_with=prefix)
            return [blob.name for blob in blobs]
        except Exception as e:
            logger.error(f"Erro ao listar blobs: {str(e)}")
            raise

    def update_metadata(self, blob_path, new_metadata):
        """
        Atualiza metadados de um blob existente
        
        Args:
            blob_path (str): Caminho completo do blob
            new_metadata (dict): Novos metadados
            
        Returns:
            bool: True se a atualização foi bem-sucedida
        """
        try:
            blob_client = self.container_client.get_blob_client(blob_path)
            existing_properties = blob_client.get_blob_properties()
            
            # Mantém os metadados existentes e adiciona/atualiza com os novos
            metadata = existing_properties.metadata
            metadata.update(new_metadata)
            
            blob_client.set_blob_metadata(metadata=metadata)
            return True
        except Exception as e:
            logger.error(f"Erro ao atualizar metadados: {str(e)}")
            raise

    def generate_sas_url(self, blob_path, expiry_hours=1):
        """
        Gera uma URL assinada (SAS) temporária para um blob
        
        Args:
            blob_path (str): Caminho completo do blob
            expiry_hours (int): Horas até a expiração do link
            
        Returns:
            str: URL assinada
        """
        try:
            blob_client = self.container_client.get_blob_client(blob_path)
            
            # Define a expiração
            expiry_time = datetime.utcnow() + timedelta(hours=expiry_hours)
            
            # Gera o token SAS com permissões de leitura
            sas_token = generate_blob_sas(
                account_name=self.blob_service_client.account_name,
                container_name=self.container_name,
                blob_name=blob_path,
                account_key=self.blob_service_client.credential.account_key,
                permission=BlobSasPermissions(read=True),
                expiry=expiry_time
            )
            
            return f"{blob_client.url}?{sas_token}"
        except Exception as e:
            logger.error(f"Erro ao gerar URL SAS: {str(e)}")
            raise

if __name__ == "__main__":
    # Configuração (substitua com suas credenciais)
    ACCOUNT_URL = "https://<seu_storage_account>.blob.core.windows.net"
    CONTAINER_NAME = "ecommerce-data"
    
    # Inicializa o cliente
    ecommerce_storage = EcommerceBlobStorage(ACCOUNT_URL, CONTAINER_NAME)
    
    # Exemplo 1: Armazenar um produto
    product_data = {
        "id": "prod_12345",
        "name": "Smartphone Premium",
        "price": 999.99,
        "category": "Eletrônicos",
        "stock": 50,
        "description": "O mais recente smartphone com câmera de 108MP"
    }
    
    product_path = ecommerce_storage.upload_data(
        data=product_data,
        data_type="product",
        identifier="prod_12345",
        metadata={"created_by": "user123", "department": "inventory"}
    )
    print(f"Produto armazenado em: {product_path}")
    
    # Exemplo 2: Armazenar uma imagem do produto
    with open("smartphone_image.jpg", "rb") as image_file:
        image_data = image_file.read()
    
    image_path = ecommerce_storage.upload_data(
        data=image_data,
        data_type="image",
        identifier="prod_12345_image1",
        file_extension="jpg"
    )
    print(f"Imagem armazenada em: {image_path}")
    
    # Exemplo 3: Recuperar dados do produto
    retrieved_product = ecommerce_storage.download_data(product_path)
    print("Produto recuperado:", retrieved_product)
    
    # Exemplo 4: Listar todos os produtos
    products = ecommerce_storage.list_data(data_type="product")
    print("Lista de produtos:", products)
    
    # Exemplo 5: Gerar URL temporária para a imagem
    image_url = ecommerce_storage.generate_sas_url(image_path, expiry_hours=24)
    print("URL temporária da imagem:", image_url)
