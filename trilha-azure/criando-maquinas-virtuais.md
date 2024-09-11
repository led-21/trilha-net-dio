# Criando máquinas Virtuais na Azure
Criar Máquinas Virtuais (VMs) no Microsoft Azure é um processo que pode ser feito de forma relativamente simples através do portal do Azure, da linha de comando (CLI), ou utilizando scripts (PowerShell, ARM templates, etc.). Vou detalhar o passo a passo para criar uma VM utilizando o Portal do Azure:

## Passo a Passo para Criar uma Máquina Virtual no Portal do Azure
### Acessar o Portal do Azure
- Acesse o Portal do Azure e faça login com suas credenciais.

### Criar um Novo Recurso
- No menu de navegação esquerdo, clique em "Create a resource" (Criar um recurso).
- Selecione "Virtual Machine" ou busque por "Virtual Machine" na barra de pesquisa.

### Configurar as Informações Básicas da VM
- Subscription (Assinatura): Escolha a assinatura que será utilizada para a criação da VM.
- Resource Group (Grupo de Recursos): Escolha um grupo de recursos existente ou crie um novo para organizar a VM.
- Virtual Machine Name (Nome da Máquina Virtual): Defina o nome da VM.
- Region (Região): Escolha a localização geográfica do datacenter onde sua VM será criada.
- Availability Options: Escolha opções de disponibilidade, como conjuntos de disponibilidade ou zonas de disponibilidade para alta disponibilidade.
- Image (Imagem): Selecione o sistema operacional da VM (ex.: Windows, Ubuntu, etc.).
- Size (Tamanho): Escolha o tamanho da VM com base na quantidade de CPU, RAM, e outras especificações que você precisa.

### Configurar as Configurações de Administrador
- Authentication Type (Tipo de Autenticação): Escolha entre senha ou chave SSH.
- Username: Defina o nome de usuário para acesso à VM.
- Password/SSH Public Key: Se escolher senha, defina uma senha segura; se usar chave SSH, insira a chave pública.

### Configurar o Disco de Armazenamento
- Escolha o tipo de disco para a VM, como SSD padrão, SSD Premium, ou HDD.
- Você pode adicionar discos adicionais, se necessário.

### Configurar Rede
- Virtual Network: Selecione ou crie uma rede virtual onde a VM estará conectada.
- Subnet: Escolha uma sub-rede para a VM.
- Public IP: Se precisar de acesso à VM pela internet, configure um IP público.
- Network Security Group: Configure regras de firewall para gerenciar o tráfego de entrada e saída.

### Configurar Regras de Entrada e Monitoramento
- Defina se deseja permitir portas específicas, como SSH (22) para Linux ou RDP (3389) para Windows.
- Configure opções de monitoramento, como o Azure Monitor, para acompanhar a performance da VM.

### Revisar e Criar
- Revise todas as configurações feitas para garantir que tudo esteja correto.
- Clique em "Create" (Criar) para iniciar o processo de criação da VM.

## Após a Criação
- Assim que a VM estiver pronta, você pode acessá-la usando o método configurado (SSH ou RDP).
- Gerencie a VM através do portal, CLI, ou APIs, ajustando recursos, monitoramento, e segurança conforme necessário.
