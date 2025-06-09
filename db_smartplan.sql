CREATE DATABASE IF NOT EXISTS smartplan;
USE smartplan;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE questoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    enunciado TEXT NOT NULL,
    alternativas JSON NOT NULL,
    correta INT NOT NULL,
    disciplina VARCHAR(50) NOT NULL,
    assunto VARCHAR(100) NOT NULL,
    dificuldade VARCHAR(20) NOT NULL
);

CREATE TABLE listas_questoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL
);

CREATE TABLE lista_questoes_relacao (
    lista_id INT,
    questao_id INT,
    PRIMARY KEY (lista_id, questao_id),
    FOREIGN KEY (lista_id) REFERENCES listas_questoes(id),
    FOREIGN KEY (questao_id) REFERENCES questoes(id)
);
