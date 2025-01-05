using System.Net;
using System.Text.Json;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;

namespace ValidaçãoCPF
{
    public class CPFValidator
    {
        private readonly ILogger _logger;

        public CPFValidator(ILoggerFactory loggerFactory)
        {
            _logger = loggerFactory.CreateLogger<CPFValidator>();
        }

        [Function("ValidateCPF")]
        public HttpResponseData ValidateCPF([HttpTrigger(AuthorizationLevel.Function, "post")] HttpRequestData req)
        {
            _logger.LogInformation("C# HTTP trigger function processed a CPF validation request.");

            var requestBody = new StreamReader(req.Body).ReadToEnd();
            var data = JsonSerializer.Deserialize<Dictionary<string, string>>(requestBody);
            var cpf = data["cpf"];

            var response = req.CreateResponse(HttpStatusCode.OK);
            response.Headers.Add("Content-Type", "application/json; charset=utf-8");

            if (IsValidCPF(cpf))
            {
                response.WriteString(JsonSerializer.Serialize(new { validCPF = true }));
            }
            else
            {
                response.WriteString(JsonSerializer.Serialize(new { validCPF = false }));
            }

            return response;
        }

        private bool IsValidCPF(string cpf)
        {
            if (cpf.Length != 11 || !long.TryParse(cpf, out _))
                return false;

            var tempCpf = cpf.Substring(0, 9);
            var sum = 0;

            for (var i = 0; i < 9; i++)
                sum += (tempCpf[i] - '0') * (10 - i);

            var remainder = sum % 11;
            if (remainder < 2)
                remainder = 0;
            else
                remainder = 11 - remainder;

            var digit = remainder.ToString();
            tempCpf += digit;

            sum = 0;
            for (var i = 0; i < 10; i++)
                sum += (tempCpf[i] - '0') * (11 - i);

            remainder = sum % 11;
            if (remainder < 2)
                remainder = 0;
            else
                remainder = 11 - remainder;

            digit += remainder.ToString();

            return cpf.EndsWith(digit);
        }
    }
}
