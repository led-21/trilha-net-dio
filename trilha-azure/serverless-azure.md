# Aplicações Serverless no Azure
As aplicações serverless permitem que você desenvolva e execute aplicativos sem se preocupar com a infraestrutura subjacente. No Azure, isso é facilitado por serviços como Azure Functions e Azure Logic Apps.

## Azure Logic Apps
O Azure Logic Apps é um serviço que ajuda a automatizar e orquestrar tarefas e fluxos de trabalho entre diferentes serviços e aplicativos. 
Você pode criar fluxos de trabalho complexos usando um designer visual, conectando-se a centenas de serviços, como Office 365, SQL Server, e muitos outros. 
É ideal para integrar sistemas e automatizar processos de negócios sem escrever muito código.

## Azure Functions
As Azure Functions permitem executar pequenos pedaços de código (funções) em resposta a eventos, como uma solicitação HTTP ou uma mensagem em uma fila. 
Elas são altamente escaláveis e você paga apenas pelo tempo de execução do código. 
As Azure Functions são ótimas para tarefas como processamento de dados em tempo real, automação de tarefas e construção de APIs serverless.

## Azure Functions Database
Embora não exista um serviço específico chamado “Azure Functions Database”, as Azure Functions podem interagir com vários serviços de banco de dados no Azure, como Azure SQL Database, Cosmos DB, e Table Storage. 
Isso permite que você crie funções que leem e escrevem dados em bancos de dados, facilitando a construção de aplicativos dinâmicos e baseados em dados.

## Azure Service Bus
O Azure Service Bus é um serviço de mensagens que permite a comunicação entre diferentes partes de um aplicativo distribuído. 
Ele é usado para garantir a entrega confiável de mensagens entre serviços e componentes, mesmo em cenários de alta carga e complexidade. 
O Service Bus suporta filas, tópicos e assinaturas, permitindo padrões avançados de mensagens e integração.
