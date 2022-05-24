CREATE TABLE s (
   id INT PRIMARY KEY,
   hash varchar(100) NOT NULL,
   timestamp TIMESTAMP NOT NULL
);

CREATE TABLE a (
   id_a SERIAL PRIMARY KEY,
   id INT NOT NULL,
   hash varchar(100) NOT NULL,
   timestamp TIMESTAMP NOT NULL,
   answer varchar(100)
);