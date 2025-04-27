def validar_boleto(numero):
    """
    Valida um boleto bancário (tanto linha digitável quanto código de barras)
    
    Args:
        numero (str): Número do boleto (com ou sem formatação)
        
    Returns:
        tuple: (bool, str) indicando se é válido e mensagem de detalhes
    """
    # Remove caracteres não numéricos
    numero = ''.join(filter(str.isdigit, numero))
    
    if not numero:
        return False, "Número do boleto vazio"
    
    # Verifica o tipo de boleto (47 ou 44 dígitos)
    if len(numero) == 47:
        return validar_linha_digitavel(numero)
    elif len(numero) == 44:
        return validar_codigo_barras(numero)
    else:
        return False, f"Tamanho inválido ({len(numero)} dígitos). Boletos devem ter 44 (código de barras) ou 47 (linha digitável) dígitos."

def validar_linha_digitavel(numero):
    """Valida a linha digitável de 47 caracteres"""
    # Verifica o dígito verificador de cada campo
    campos = [
        (numero[:9], numero[9]),
        (numero[10:20], numero[20]),
        (numero[21:31], numero[31]),
    ]
    
    for campo, dv in campos:
        if not calcular_digito_verificador(campo) == dv:
            return False, f"Dígito verificador inválido no campo {campo}{dv}"
    
    # Verifica o dígito verificador geral (posição 32)
    dv_geral = numero[32]
    base_calculo = numero[:4] + numero[5:9] + numero[10:20] + numero[21:31]
    if not calcular_digito_verificador(base_calculo) == dv_geral:
        return False, f"Dígito verificador geral inválido: {dv_geral}"
    
    return True, "Linha digitável válida"

def validar_codigo_barras(numero):
    """Valida o código de barras de 44 caracteres"""
    # Verifica o dígito verificador (posição 4)
    dv = numero[4]
    base_cal
