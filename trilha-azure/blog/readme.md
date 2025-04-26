# Implantação na Azure
Passo a passo para implantação:

## 1. Criar um Azure Container Registry (ACR)
```bash
az acr create --resource-group MyResourceGroup --name myacr --sku Basic
```

## 2. Build da imagem Docker e push para o ACR:
```bash
az acr build --registry myacr --image blog-app:latest .
```

## 3. Criar um Azure Database for PostgreSQL:
```bash
az postgres flexible-server create --resource-group MyResourceGroup --name my-postgres-server --admin-user adminuser --admin-password yourpassword --sku-name Standard_B1ms --tier Burstable --version 13 --storage-size 32
```

## 4. Criar um Azure App Service ou Container App:
#### Opção A - App Service:
```bash
az webapp create --resource-group MyResourceGroup --plan MyAppServicePlan --name my-blog-app --deployment-container-image-name myacr.azurecr.io/blog-app:latest
```
#### Opção B - Container Apps:
```bash
az containerapp create --name my-blog-app --resource-group MyResourceGroup --image myacr.azurecr.io/blog-app:latest --environment MyContainerAppEnv --ingress external --target-port 5000
```

## 5. Configurar variáveis de ambiente:
```bash
az webapp config appsettings set --resource-group MyResourceGroup --name my-blog-app --settings DATABASE_URL="postgresql://adminuser:yourpassword@my-postgres-server.postgres.database.azure.com/blogdb?sslmode=require"
```
