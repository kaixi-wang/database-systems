CREATE TABLE T1 (NAME VARCHAR(15), LOCATION geometry);
INSERT INTO T1 (NAME,LOCATION)
VALUES('Building', ST_GeomFromText('POINT(-118.25747777777778 34.046275)')),
('WholeFoods', ST_GeomFromText('POINT(-118.25790277777777 34.045880555555556)')),
('XLouie', ST_GeomFromText('POINT(-118.25675833333334 34.04723611111111)')),
('Taqueria', ST_GeomFromText('POINT(-118.25604166666666 34.047016666666664)')),
('8thHope', ST_GeomFromText('POINT(-118.25908611111112 34.04663333333333)')),
('Bank', ST_GeomFromText('POINT(-118.25561388888889 34.048455555555556)')),
('Starbucks', ST_GeomFromText('POINT(-118.25530277777777 34.04884444444444)')),
('5thGrand', ST_GeomFromText('POINT(-118.25391388888889 34.050261111111105)')),
('WilshireGrand', ST_GeomFromText('POINT(-118.25620277777777 34.04787777777778)'));

SELECT ST_AsText(ST_ConvexHull(ST_Collect(location))) FROM T1;

 --POLYGON((-118.257902777778 34.0458805555556,-118.259086111111 34.0466333333333,-118.253913888889 34.0502611111111,-118.256041666667 34.0470166666667,-118.257902777778 34.0458805555556))

SELECT nn2.NAME
FROM T1 AS nn1, T1 AS nn2
WHERE nn1.NAME='AptBld' AND nn1.NAME<>nn2.NAME
ORDER BY ST_DISTANCE(nn1.location,nn2.location)
LIMIT 3

--WholeFoods
--XLouie
--Taqueria