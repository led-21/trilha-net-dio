# Gerenciamento de Máquinas Virtuais no Microsoft Azure

Bem-vindo ao repositório dedicado ao aprendizado e prática de gerenciamento de máquinas virtuais (VMs) no Microsoft Azure. Este documento serve como um guia prático, contendo resumos, anotações e dicas baseadas na [documentação oficial da Microsoft](https://docs.microsoft.com/azure/virtual-machines), com o objetivo de apoiar estudos e implementações futuras.

## Objetivo do Repositório

Este repositório foi criado como parte de um desafio prático para:
- Aplicar conceitos de gerenciamento de VMs no Azure em um ambiente prático.
- Documentar processos técnicos de forma clara e estruturada.
- Utilizar o GitHub como ferramenta para compartilhamento de documentação técnica.

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
