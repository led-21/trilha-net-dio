# Verificação de boletos bancários
## Funcionalidades Implementadas
Validação de boletos bancários nos formatos:
- Linha digitável (47 caracteres)
- Código de barras (44 caracteres)

Verificação de:
- Dígitos verificadores (módulo 10 e módulo 11)
- Tamanho do número do boleto
- Formatação básica

Interface do usuário:
- Entrada do número do boleto (com ou sem formatação)
- Exibição de resultados claros (válido/inválido)
- Formatação do boleto para exibição

## Instale as dependências necessárias
```bash
pip install flask
```

## Execute a aplicação
```bash
python app.py
```

## Acesse a interface no navegador
```bash
http://localhost:5000
```
