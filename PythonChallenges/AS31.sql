SELECT matchid, player FROM goal 
  WHERE teamid = 'GER'
  SELECT id,stadium,team1,team2
  FROM game
where id = 1012
SELECT player,teamid, stadium, mdate
  FROM game JOIN goal ON (id=matchid)
WHERE teamid = 'GER'
SELECT team1,team2, player
  FROM game JOIN goal ON (id=matchid)
WHERE player LIKE 'Mario%'
SELECT player, teamid, coach, gtime
  FROM goal JOIN  eteam ON teamid=id
 WHERE gtime<=10
 SELECT mdate, teamname
FROM game JOIN eteam ON (team1=eteam.id)
WHERE coach = 'Fernando Santos'
SELECT player 
FROM goal JOIN game ON matchid = id
WHERE stadium = 'National Stadium, Warsaw'
SELECT player
  FROM game JOIN goal ON matchid = id 
    WHERE (team1='GER' AND team2='GRE')
