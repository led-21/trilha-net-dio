-- 1 - Buscar o nome e ano dos filmes
SELECT Nome, Ano FROM Filmes

-- 2 - Buscar o nome e ano dos filmes, ordenados por ordem crescente pelo ano
SELECT Nome, Ano FROM Filmes 
ORDER BY Ano

-- 4 - Buscar os filmes lançados em 1997
SELECT * FROM Filmes 
WHERE Ano = 1997

-- 5 - Buscar os filmes lançados APÓS o ano 2000
SELECT * FROM Filmes 
WHERE Ano > 2000

-- 6 - Buscar os filmes com a duracao maior que 100 e menor que 150, ordenando pela duracao em ordem crescente
SELECT * FROM Filmes 
WHERE Duracao > 100 AND Duracao < 150
ORDER BY Duracao

-- 7 - Buscar a quantidade de filmes lançadas no ano, agrupando por ano, ordenando em ordem decrescente
SELECT Ano, COUNT(*) as N FROM Filmes 
GROUP BY Ano
ORDER BY N DESC

-- 8 - Buscar os Atores do gênero masculino, retornando o PrimeiroNome, UltimoNome
SELECT PrimeiroNome, UltimoNome, Genero FROM Atores
WHERE Genero = 'M'

-- 9 - Buscar os Atores do gênero feminino, retornando o PrimeiroNome, UltimoNome, e ordenando pelo PrimeiroNome
SELECT PrimeiroNome, UltimoNome, Genero FROM Atores
WHERE Genero = 'F'
ORDER BY PrimeiroNome

-- 10 - Buscar o nome do filme e o gênero
WITH GeneroFilme AS (SELECT FilmesGenero.IdFilme, Genero FROM FilmesGenero
INNER JOIN Generos ON Generos.Id = FilmesGenero.IdGenero)

SELECT Nome, Genero FROM Filmes
INNER JOIN GeneroFilme ON Filmes.id = GeneroFilme.IdFilme

-- 11 - Buscar o nome do filme e o gênero do tipo "Mistério"
WITH GeneroFilme AS (SELECT FilmesGenero.IdFilme, Genero FROM FilmesGenero
INNER JOIN Generos ON Generos.Id = FilmesGenero.IdGenero)

SELECT Nome, Genero FROM Filmes
INNER JOIN GeneroFilme ON Filmes.id = GeneroFilme.IdFilme
WHERE Genero LIKE 'Mistério'

-- 12 - Buscar o nome do filme e os atores, trazendo o PrimeiroNome, UltimoNome e seu Papel
WITH Elenco AS (SELECT ElencoFilme.IdFilme,ElencoFilme.Papel, Atores.PrimeiroNome, Atores.UltimoNome FROM Atores
INNER JOIN ElencoFilme ON Atores.Id = ElencoFilme.IdAtor)

SELECT Nome, PrimeiroNome, UltimoNome, Papel FROM Filmes
INNER JOIN Elenco ON Filmes.id = Elenco.IdFilme







