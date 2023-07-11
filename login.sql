CREATE DATABASE IF NOT EXISTS escola;

USE escola;

CREATE TABLE usuario(
codigo INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
senha VARCHAR(100) NOT NULL,
acesso INT);


INSERT INTO usuario VALUES
(1, "abel", MD5("legal"), 1);

INSERT INTO usuario VALUES
(2, "bernadete", MD5("bolo"), 2);

INSERT INTO usuario VALUES
(3, "caio", MD5("caneta"), 3);



