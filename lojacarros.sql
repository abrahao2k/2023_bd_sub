CREATE DATABASE lojacarros;

USE lojacarros;

CREATE TABLE carros(
codigo INT PRIMARY KEY AUTO_INCREMENT,
fabricante VARCHAR(100),
modelo VARCHAR(100),
preco FLOAT
);

INSERT INTO carros 
VALUES (1, "Fiat", "Mobi", 68990);

INSERT INTO carros
VALUES(NULL, "Fiat", "Pulse", 98990);

INSERT INTO carros
VALUES(5, "Fiat", "Strada", 103990);

INSERT INTO carros
VALUES(NULL, "Fiat", "Toro", 146990);

INSERT INTO carros
VALUES (3, "VW", "Gol", 55760),
(4, "VW", "Polo", 80580),
(7,"VW", "Nivus", 125890);




