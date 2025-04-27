from flask import Flask, render_template, request, jsonify
from boleto import validar_boleto

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validar', methods=['POST'])
def validar():
    numero_boleto = request.form.get('numero_boleto', '').replace('.', '').replace('-', '')
    resultado, detalhes = validar_boleto(numero_boleto)
    
    return jsonify({
        'valido': resultado,
        'detalhes': detalhes,
        'numero_formatado': formatar_boleto(numero_boleto) if resultado else numero_boleto
    })

def formatar_boleto(numero):
    # Formata o número do boleto para exibição (44 caracteres)
    if len(numero) == 44:
        return f"{numero[:5]}.{numero[5:10]} {numero[10:15]}.{numero[15:21]} {numero[21:26]}.{numero[26:32]} {numero[32:37]}.{numero[37:]}"
    elif len(numero) == 47:
        return f"{numero[:9]}.{numero[9:10]} {numero[10:20]}.{numero[20:21]} {numero[21:31]}.{numero[31:32]} {numero[32:47]}"
    return numero

if __name__ == '__main__':
    app.run(debug=True)
