# Gerenciamento de Máquinas Virtuais no Microsoft Azure

## O que são Máquinas Virtuais no Azure?

Máquinas virtuais no Azure são recursos computacionais que permitem executar sistemas operacionais e aplicativos em um ambiente virtualizado na nuvem. Elas oferecem flexibilidade para configurar sistemas Windows ou Linux, com opções de dimensionamento, armazenamento e rede.

### Benefícios
- *Escalabilidade*: Ajuste recursos (CPU, memória, armazenamento) conforme a demanda.
- *Flexibilidade*: Suporte a diferentes sistemas operacionais e cargas de trabalho.
- *Gerenciamento simplificado*: Ferramentas como Azure Portal, CLI e PowerShell facilitam a administração.
- *Alta disponibilidade*: Recursos como conjuntos de disponibilidade e zonas de disponibilidade garantem resiliência.

## Pré-requisitos

Antes de começar, certifique-se de ter:
- Uma *conta ativa no Azure* (crie uma conta gratuita em [azure.microsoft.com](https://azure.microsoft.com)).
- Familiaridade com conceitos básicos de computação em nuvem.
- Ferramentas instaladas:
  - [Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli) ou [Azure PowerShell](https://docs.microsoft.com/powershell/azure/install-az-ps).
  - [Git](https://git-scm.com/downloads) para versionamento.
- Conhecimento básico de Markdown para edição deste README.

## Passos para Gerenciamento de VMs no Azure

A seguir, detalhamos os principais processos para criar, gerenciar e monitorar máquinas virtuais no Azure, com base na documentação oficial.

### 1. Criando uma Máquina Virtual

#### Passos no Azure Portal
1. Acesse o [Azure Portal](https://portal.azure.com).
2. No menu, clique em *Máquinas Virtuais* > *Criar* > *Máquina Virtual*.
3. Configure os detalhes básicos:
   - *Assinatura*: Escolha sua assinatura do Azure.
   - *Grupo de Recursos*: Crie ou selecione um grupo existente.
   - *Nome da VM*: Defina um nome único.
   - *Região*: Escolha a região mais próxima para menor latência.
   - *Imagem*: Selecione o sistema operacional (ex.: Windows Server, Ubuntu).
   - *Tamanho*: Escolha o tamanho da VM com base na carga de trabalho (ex.: D2s_v3 para uso geral).
4. Configure autenticação (senha ou chave SSH para Linux).
5. Defina configurações de rede (rede virtual, sub-rede, IP público).
6. Revise e clique em *Criar*.

#### Usando Azure CLI
```bash
az vm create \
  --resource-group myResourceGroup \
  --name myVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --generate-ssh-keys \
  --location eastus
```

### 2. Conectando-se à Máquina Virtual
Para VMs Windows:
No Azure Portal, navegue até a VM criada

Clique em "Conectar" > "RDP"

Baixe o arquivo RDP e abra-o

Insira as credenciais de administrador configuradas durante a criação

Para VMs Linux:
```bash
ssh azureuser@<public-ip-address> -i ~/.ssh/id_rsa
3. Gerenciamento de Discos
Adicionar um disco de dados:
bash
az vm disk attach \
  --resource-group myResourceGroup \
  --vm-name myVM \
  --disk myDataDisk \
  --size-gb 128 \
  --sku StandardSSD_LRS \
  --new
```

### 3. Listar discos conectados:
```bash
az vm show \
  --resource-group myResourceGroup \
  --name myVM \
  --query "storageProfile.dataDisks"
```

### 4. Monitoramento e Diagnóstico
Habilite o monitoramento avançado:

```bash
az vm boot-diagnostics enable \
  --resource-group myResourceGroup \
  --name myVM
```

Visualize métricas comuns:

```bash
az monitor metrics list \
  --resource /subscriptions/{sub-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVM \
  --metric "Percentage CPU" "Available Memory Bytes"
```

### 5. Operações Básicas de Manutenção
Reiniciar uma VM:

```bash
az vm restart \
  --resource-group myResourceGroup \
  --name myVM
```

Parar (desalocar) uma VM:
```bash
az vm deallocate \
  --resource-group myResourceGroup \
  --name myVM
```

Redimensionar uma VM:

```bash
az vm resize \
  --resource-group myResourceGroup \
  --name myVM \
  --size Standard_D4s_v3
```
### 6. Configuração de Rede
Adicionar uma regra de NSG:
```bash
az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name myVMNSG \
  --name allow-http \
  --access allow \
  --protocol Tcp \
  --direction Inbound \
  --priority 100 \
  --source-address-prefix "*" \
  --source-port-range "*" \
  --destination-address-prefix "*" \
  --destination-port-range 80
```

###  7. Automação com Scripts
Exemplo de script completo para criação de VM:

```bash
#!/bin/bash

# Configurações
RESOURCE_GROUP="myResourceGroup"
LOCATION="eastus"
VM_NAME="myAutomatedVM"
ADMIN_USER="azureuser"
IMAGE="UbuntuLTS"
SIZE="Standard_B1s"
```

Criar grupo de recursos
```bash
az group create --name $RESOURCE_GROUP --location $LOCATION
```

Criar VM
```bash
az vm create \
  --resource-group $RESOURCE_GROUP \
  --name $VM_NAME \
  --image $IMAGE \
  --admin-username $ADMIN_USER \
  --generate-ssh-keys \
  --size $SIZE \
  --public-ip-sku Standard
```

Abrir porta 80 para tráfego web
```bash
az vm open-port \
  --resource-group $RESOURCE_GROUP \
  --name $VM_NAME \
  --port 80
```

Instalar servidor web (usando extensão de script personalizado)

```bash
az vm extension set \
  --resource-group $RESOURCE_GROUP \
  --vm-name $VM_NAME \
  --name customScript \
  --publisher Microsoft.Azure.Extensions \
  --settings '{"commandToExecute":"apt-get update && apt-get install -y nginx"}'
```

### 8. Melhores Práticas
Tags: Use tags para organização

```bash
az vm update \
  --resource-group myResourceGroup \
  --name myVM \
  --set tags.Department=Finance tags.Environment=Production
```

Backup: Configure backup regular

```bash
az backup vault create \
  --resource-group myResourceGroup \
  --name myRecoveryServicesVault \
  --location eastus
```

Atualizações: Gerencie patches com Update Management

```bash
az vm extension set \
  --resource-group myResourceGroup \
  --vm-name myVM \
  --name OmsAgentForLinux \
  --publisher Microsoft.EnterpriseCloud.Monitoring
```

### 9. Limpeza de Recursos
Para excluir recursos quando não forem mais necessários:

```bash
az group delete --name myResourceGroup --yes --no-wait
```

# Referências Úteis para Gerenciamento de VMs no Azure

## Documentação Oficial
- [Documentação de Máquinas Virtuais Azure](https://docs.microsoft.com/azure/virtual-machines/) - Guia completo sobre criação, configuração e gerenciamento de VMs
- [Azure CLI Reference](https://docs.microsoft.com/cli/azure/reference-index) - Referência completa de comandos da CLI

## Ferramentas e Serviços
- [Galeria de Imagens Azure](https://azuremarketplace.microsoft.com/) - Catálogo de imagens disponíveis para VMs
- [Calculadora de Custos Azure](https://azure.microsoft.com/pricing/calculator/) - Estime custos de recursos na nuvem
- [Azure Architecture Center](https://docs.microsoft.com/azure/architecture/) - Melhores práticas de arquitetura

## Tutoriais e Guias
- [Quickstart: Criar VM Linux](https://docs.microsoft.com/azure/virtual-machines/linux/quick-create-cli)
- [Quickstart: Criar VM Windows](https://docs.microsoft.com/azure/virtual-machines/windows/quick-create-cli)
