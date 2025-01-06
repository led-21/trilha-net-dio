using Microsoft.Azure.Cosmos;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var host = new HostBuilder()
    .ConfigureFunctionsWorkerDefaults()
    .ConfigureServices(services =>
    {
        services.AddApplicationInsightsTelemetryWorkerService();
        services.ConfigureFunctionsApplicationInsights();
    })
    .ConfigureServices((context, services) =>
    {
        var configuration = context.Configuration;
        var cosmosDbConnectionString = configuration["CosmosDbConnectionString"];
        var cosmosClient = new CosmosClient(cosmosDbConnectionString);
        services.AddSingleton(cosmosClient);
    })
    .Build();

host.Run();
