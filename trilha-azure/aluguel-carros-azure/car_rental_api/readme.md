# Passos para Deploy
## Criar um Resource Group no Azure
```bash
az group create --name AluguelCarrosRG --location eastus
```

## Criar Azure Functions
```bash
az functionapp create \
    --name aluguel-carros-api \
    --resource-group AluguelCarrosRG \
    --runtime python \
    --runtime-version 3.9 \
    --consumption-plan-location eastus \
    --os-type Linux \
    --storage-account <storage_account_name>
```

## Configurar Variáveis de Ambiente
```bash
az functionapp config appsettings set \
    --name aluguel-carros-api \
    --resource-group AluguelCarrosRG \
    --settings \
        AZURE_KEY_VAULT_URL="https://<keyvault-name>.vault.azure.net/" \
        AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=..."
```

## Fazer Deploy do Código
```bash
func azure functionapp publish aluguel-carros-api
```
