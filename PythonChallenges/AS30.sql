SELECT name, continent, population FROM world
SELECT name FROM world
WHERE population > 200000000
SELECT name, gdp/population
FROM world
WHERE population > 200000000
SELECT name, population/1000000
FROM world
WHERE continent LIKE 'South America'
SELECT name, population
FROM world
WHERE name LIKE 'France' or name LIKE 'Germany' or name LIKE 'Italy'
SELECT name
FROM world
WHERE name LIKE '%united%'
SELECT name, population, area
FROM world
WHERE population > 250000000 or area > 3000000
SELECT name
    , population
    , area
FROM world
WHERE (area > 3000000 AND population <= 250000000)
OR (area <= 3000000 AND population > 250000000)
SELECT name, ROUND(population/1000000,2),ROUND(gdp/1000000000,2)
FROM world 
WHERE continent LIKE 'South America' 
SELECT name, round(gdp/population,-3) FROM world
WHERE gdp > 1000000000000
SELECT name, capital FROM world
WHERE len(name) = len(capital)
SELECT name, capital
FROM world
WHERE LEFT(name, 1) = LEFT(capital,1) and name <> capital
SELECT name
   FROM world
WHERE name LIKE '%o%a%i%u%e%'
