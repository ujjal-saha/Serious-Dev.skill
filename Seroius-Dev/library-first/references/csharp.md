# C# / .NET packages

Install with `dotnet add package <name>`. This updates the `.csproj` file.
Check first whether .NET already does the job: `System.Text.Json` (JSON), `HttpClient` (HTTP), `System.IO`, `System.Linq`, `System.Text.RegularExpressions`, `Task` and `async/await`, `System.Threading.Channels`.

| Package | Install | Use it for |
|---|---|---|
| Newtonsoft.Json | dotnet add package Newtonsoft.Json | flexible JSON read and write |
| Dapper | dotnet add package Dapper | fast simple SQL queries into objects |
| Microsoft.EntityFrameworkCore | dotnet add package Microsoft.EntityFrameworkCore | database ORM (also add a provider, for example Microsoft.EntityFrameworkCore.Sqlite) |
| Serilog | dotnet add package Serilog | structured logging |
| Polly | dotnet add package Polly | retry, timeout, circuit breaker for failing calls |
| RestSharp | dotnet add package RestSharp | easy REST API calls |
| CsvHelper | dotnet add package CsvHelper | read and write CSV files |
| ClosedXML | dotnet add package ClosedXML | read and write Excel xlsx files |
| HtmlAgilityPack | dotnet add package HtmlAgilityPack | parse HTML, scrape pages |
| AutoMapper | dotnet add package AutoMapper | copy data between similar objects |
| FluentValidation | dotnet add package FluentValidation | validation rules for objects |
| SixLabors.ImageSharp | dotnet add package SixLabors.ImageSharp | open, resize, edit images (check license) |
| QuestPDF | dotnet add package QuestPDF | create PDF files from code (check license) |
| Spectre.Console | dotnet add package Spectre.Console | nice terminal output, tables, progress, prompts |
| xunit | dotnet add package xunit | unit tests |
| Moq | dotnet add package Moq | fake objects for tests |
