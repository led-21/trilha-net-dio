import unittest
from boleto import *

class TestBoletoValidator(unittest.TestCase):
    def test_validar_linha_digitavel_valida(self):
        # Boleto de exemplo válido (usar um real para testes completos)
        boleto_valido = "34191.09008 01013.510047 91020.150008 6 84190026000"
        self.assertTrue(validar_boleto(boleto_valido)[0])
    
    def test_validar_codigo_barras_valido(self):
        # Código de barras válido (usar um real para testes completos)
        codigo_valido = "34196841900260001090001013510049102015000"
        self.assertTrue(validar_boleto(codigo_valido)[0])
    
    def test_validar_linha_digitavel_invalida(self):
        # Boleto com dígito verificador inválido
        boleto_invalido = "34191.09008 01013.510047 91020.150008 7 84190026000"
        self.assertFalse(validar_boleto(boleto_invalido)[0])
    
    def test_validar_codigo_barras_invalido(self):
        # Código de barras com dígito verificador inválido
        codigo_invalido = "34195841900260001090001013510049102015000"
        self.assertFalse(validar_boleto(codigo_invalido)[0])
    
    def test_calcular_digito_verificador(self):
        self.assertEqual(calcular_digito_verificador("12345678"), "2")
    
    def test_calcular_digito_verificador_mod11(self):
        self.assertEqual(calcular_digito_verificador_mod11("12345678"), "7")

if __name__ == '__main__':
    unittest.main()
