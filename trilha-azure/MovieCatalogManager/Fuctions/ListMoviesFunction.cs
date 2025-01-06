using System.Net;
using System.Text.Json;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;
using Microsoft.Azure.Cosmos;
using MovieCatalogManager.Models;

namespace MovieCatalogManager.Fuctions
{
    public class ListMoviesFunction
    {
        private readonly ILogger _logger;
        private readonly CosmosClient _cosmosClient;
        private readonly Container _container;

        public ListMoviesFunction(ILoggerFactory loggerFactory, CosmosClient cosmosClient)
        {
            _logger = loggerFactory.CreateLogger<ListMoviesFunction>();
            _cosmosClient = cosmosClient;
            _container = _cosmosClient.GetContainer("MovieCatalogDB", "Movies");
        }

        [Function("ListMovies")]
        public async Task<HttpResponseData> Run([HttpTrigger(AuthorizationLevel.Function, "get")] HttpRequestData req)
        {
            _logger.LogInformation("C# HTTP trigger function processed a request to list movies.");

            var queryDefinition = new QueryDefinition("SELECT * FROM c");
            var iterator = _container.GetItemQueryIterator<Movie>(queryDefinition);
            var movies = new List<Movie>();

            while (iterator.HasMoreResults)
            {
                var response = await iterator.ReadNextAsync();
                movies.AddRange(response.ToList());
            }

            var responseMessage = req.CreateResponse(HttpStatusCode.OK);
            responseMessage.Headers.Add("Content-Type", "application/json; charset=utf-8");
            await responseMessage.WriteStringAsync(JsonSerializer.Serialize(movies));

            return responseMessage;
        }
    }
}
