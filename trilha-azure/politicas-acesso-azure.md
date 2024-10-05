## Gerenciar políticas de acesso no Azure

### Controle de Acesso Baseado em Função (RBAC)
- Definição de Funções: RBAC permite atribuir permissões específicas a usuários, grupos e aplicativos com base em suas funções dentro da organização.
- Atribuição de Funções: Você pode atribuir funções a nível de assinatura, grupo de recursos ou recurso individual.
- Privilégios Mínimos: Seguir o princípio de privilégios mínimos garante que os usuários tenham apenas as permissões necessárias para realizar suas tarefas.

### Políticas do Azure (Azure Policy)
- Definição de Políticas: Azure Policy permite criar, atribuir e gerenciar políticas que aplicam regras e efeitos aos recursos do Azure, garantindo que eles estejam em conformidade com os padrões corporativos.
- Iniciativas de Políticas: Agrupe várias políticas em uma única iniciativa para simplificar a gestão e a aplicação de políticas em larga escala.

### Acesso Condicional
- Configuração de Políticas de Acesso Condicional: Defina políticas que controlam o acesso com base em condições específicas, como localização, dispositivo e risco de login.
- Autenticação Multifator (MFA): Adicione uma camada extra de segurança exigindo mais de uma forma de verificação para acessar recursos.

### Monitoramento e Auditoria
- Azure Monitor: Use o Azure Monitor para rastrear e registrar atividades de acesso e alterações de configuração.
- Azure Security Center: Oferece uma visão unificada da segurança de seus recursos no Azure, fornecendo recomendações e alertas para melhorar sua postura de segurança.

### Práticas Recomendadas
- Revisões de Acesso: Realize revisões periódicas de acesso para garantir que apenas os usuários autorizados tenham acesso a recursos críticos.
- Centralizar o Gerenciamento de Identidade: Gerencie todas as identidades de forma centralizada para simplificar a administração e melhorar a segurança.
