## Configurando Recursos e Dimensionamentos em Máquinas Virtuais na Azure

### Acessar o Portal do Azure:
- Faça login no Portal do Azure.

### Criar uma Máquina Virtual:
- No painel, procure por “Máquinas Virtuais” e clique em “Criar”.
- Selecione a assinatura e o grupo de recursos.
- Defina o nome da VM, a região e a imagem do sistema operacional (Windows ou Linux).
- Configure as credenciais de login (usuário e senha para Windows, chaves SSH para Linux).

### Configurar o Tamanho da Máquina Virtual:
- Escolha o tamanho da VM com base na carga de trabalho esperada:
  - Tamanhos Gerais: Para aplicações comuns.
  - Tamanhos Otimizados para Memória: Para bancos de dados e aplicações que exigem muita RAM.
  - Tamanhos Otimizados para Computação: Para cargas que exigem alto poder de processamento.

### Configurar o Armazenamento:
- Na aba de discos, selecione o tipo de disco:
  - SSD Premium: Para alta performance.
  - SSD Padrão: Para cargas moderadas.
  - HDD Padrão: Para cargas de baixo custo.

### Configurar a Rede:
- Associe a VM a uma Rede Virtual (VNet) existente ou crie uma nova.
- Configure as opções de rede, como IP público e grupos de segurança de rede.

### Dimensionamento Automático:
- Configure a autoescala para ajustar automaticamente o número de instâncias com base na demanda.
