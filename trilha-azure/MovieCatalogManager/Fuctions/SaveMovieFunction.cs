using System.Net;
using System.Text.Json;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;
using Microsoft.Azure.Cosmos;
using MovieCatalogManager.Models;

namespace MovieCatalogManager.Fuctions
{
    public class SaveMovieFunction
    {
        private readonly ILogger _logger;
        private readonly CosmosClient _cosmosClient;
        private readonly Container _container;

        public SaveMovieFunction(ILoggerFactory loggerFactory, CosmosClient cosmosClient)
        {
            _logger = loggerFactory.CreateLogger<SaveMovieFunction>();
            _cosmosClient = cosmosClient;
            _container = _cosmosClient.GetContainer("MovieCatalogDB", "Movies");
        }

        [Function("SaveMovie")]
        public async Task<HttpResponseData> Run([HttpTrigger(AuthorizationLevel.Function, "post")] HttpRequestData req)
        {
            _logger.LogInformation("C# HTTP trigger function processed a request to save a movie.");

            string requestBody = await new StreamReader(req.Body).ReadToEndAsync();
            var movie = JsonSerializer.Deserialize<Movie>(requestBody);

            await _container.CreateItemAsync(movie, new PartitionKey(movie.id));

            var response = req.CreateResponse(HttpStatusCode.Created);
            response.Headers.Add("Content-Type", "application/json; charset=utf-8");
            await response.WriteStringAsync(JsonSerializer.Serialize(movie));

            return response;
        }
    }

}