// Importa a biblioteca de expressões regulares
using System.Text.RegularExpressions;

Console.WriteLine(
    "Digite o número do cartão de crédito e bandeira separados por espaço:" +
    "\nDigite \"teste\" para rodar os testes." +
    "\nDigite \"sair\" para encerrar");

while (true)
{
    // Entrada do usuário
    var input = Console.ReadLine();

    // Verifica se a entrada é para rodar os testes
    if (input == "teste")
    {
        TestCardValidator.RunTests();
        Console.WriteLine("Fim dos testes");
        return;
    }
    else if (input == "sair")
    {
        Console.WriteLine("Aplicativo encerrado pelo usuario");
        return;
    }

    // Valida o número do cartão e bandeira
    try
    {
        var cardData = input.Split(' ');
        (string cardNumber, string cardBrand) = (cardData[0], cardData[1]);

        if (CardValidator.IsValidCardNumber(cardNumber, cardBrand))
        {
            Console.WriteLine($"Número do cartão válido. Bandeira: {cardBrand}");
            Console.WriteLine();
        }
        else
        {
            Console.WriteLine("Número do cartão inválido.");
            Console.WriteLine();
        }
    }
    catch
    {
        Console.WriteLine("Entrada inválida. Digite o número do cartão e a bandeira separados por espaço.");
    }
}

// Classe estática para rodar os testes de validação de cartão
static class TestCardValidator
{
    // Lista de dados de teste
    static List<CardTestData> testData = new()
    {
        new ("4111111111111111", "Visa", true),
        new ("5500000000000004", "MasterCard", true),
        new ("340000000000009", "American Express", true),
        new ("30000000000004", "Diners Club", true),
        new ("6011000000000004", "Discover", true),
        new ("3530111333300000", "JCB", true),
        new ("6362970000457013", "Elo", true),
        new ("6062825624254001", "Hipercard", true),
        new ("5078601870000127980", "Aura", true),
        new ("6046220500000000", "Cabal", false),
        new ("1234567812345670", "Nulo retorna falso", false)
    };

    // Método para rodar os testes
    public static void RunTests()
    {
        foreach (var data in testData)
        {
            bool isValid = CardValidator.IsValidCardNumber(data.CardNumber, data.CardBrand);
            if (isValid == data.IsValid)
            {
                Console.WriteLine($"Teste {data.CardBrand} passou: {data.CardNumber}");
            }
            else
            {
                Console.WriteLine($"Teste {data.CardBrand} falhou: {data.CardNumber}");
            }
        }
    }
}

// Record para armazenar dados de teste
record CardTestData(string CardNumber, string CardBrand, bool IsValid);

// Classe estática para validar cartões
static class CardValidator
{
    // Método para validar o número do cartão
    public static bool IsValidCardNumber(string cardNumber, string cardBrand)
    {
        return ValidCardBrand(cardBrand, cardNumber) && IsLuhnValid(cardNumber);
    }

    // Método para validar a bandeira do cartão
    public static bool ValidCardBrand(string cardBrand, string cardNumber)
    {
        var cardBrands = new Dictionary<string, string>
        {
            { "Visa", "^4[0-9]{12}(?:[0-9]{3})?$" },
            { "MasterCard", "^5[1-5][0-9]{14}$" },
            { "American Express", "^3[47][0-9]{13}$" },
            { "Diners Club", "^3(?:0[0-5]|[68][0-9])[0-9]{11}$" },
            { "Discover", "^6(?:011|5[0-9]{2})[0-9]{12}$" },
            { "JCB", "^(?:2131|1800|35\\d{3})\\d{11}$" },
            { "Elo", "^3[0-9]{15}$" },
            { "Hipercard", "^6[0-9]{15}$" },
            { "Aura", "^5[0-9]{15}$" },
            { "Cabal", "^6[0-9]{15}$" }
        };

        if (cardBrands.ContainsKey(cardBrand))
        {
            return Regex.IsMatch(cardNumber, cardBrands[cardBrand]);
        }

        return false;
    }

    // Método para validar o número do cartão usando o algoritmo de Luhn
    static bool IsLuhnValid(string cardNumber)
    {
        int sum = 0;
        bool alternate = false;

        for (int i = cardNumber.Length - 1; i >= 0; i--)
        {
            char[] nx = cardNumber.ToCharArray();
            int n = int.Parse(nx[i].ToString());

            if (alternate)
            {
                n *= 2;
                if (n > 9)
                {
                    n -= 9;
                }
            }

            sum += n;
            alternate = !alternate;
        }

        return (sum % 10 == 0);
    }
}
