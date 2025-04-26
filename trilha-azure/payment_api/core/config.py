from pydantic import BaseSettings, AnyHttpUrl, PostgresDsn
from typing import List, Optional

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "payment-api"
    
    # Azure Key Vault para segredos (recomendado para produção)
    AZURE_KEY_VAULT_URL: Optional[str] = None
    
    # Autenticação JWT
    JWT_SECRET: str = "SECRET_KEY"  # Em produção, use Azure Key Vault
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Banco de dados - Azure Database for PostgreSQL recomendado
    DATABASE_URL: PostgresDsn = "postgresql://user:pass@localhost:5432/payments"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
