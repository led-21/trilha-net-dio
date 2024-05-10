using DesafioPOO.Models;

// TODO: Realizar os testes com as classes Nokia e Iphone
Console.WriteLine("Teste Smartphone Modelo Nokia:");
Smartphone nokia = new Nokia(numero: "98465321", modelo: "Nokia m1", imei: "0000", memoria: 16);
nokia.Ligar();
nokia.ReceberLigacao();
nokia.InstalarAplicativo("GitHub");

Console.WriteLine();

Console.WriteLine("Teste Smartphone Modelo iPhone:");
Smartphone iphone = new Iphone(numero: "4987", modelo: "Iphone 15 Pro", imei: "0000", memoria: 512);
iphone.Ligar();
iphone.ReceberLigacao();
iphone.InstalarAplicativo("LinkedIn");