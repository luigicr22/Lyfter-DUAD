CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(55) NOT NULL,
    email VARCHAR(25) UNIQUE NOT NULL
);

CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(55) NOT NULL
);

CREATE TABLE states (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    state VARCHAR(25) NOT NULL
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(55) NOT NULL,
    id_author INTEGER REFERENCES authors(id)
);

CREATE TABLE rents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_customer INTEGER NOT NULL REFERENCES customers(id),
    id_book INTEGER NOT NULL REFERENCES books(id),
    id_state INTEGER NOT NULL REFERENCES states(id)
);

INSERT INTO authors (name) VALUES
    ('Miguel de Cervantes'),
    ('Dante Alighieri'),
    ('Takehiko Inoue'),
    ('Akira Toriyama'),
    ('Walt Disney');

INSERT INTO customers (name, email) VALUES
    ('John Doe','j.doe@email.com'),
    ('Jane Doe','jane@doe.com'),
    ('Luke Skywalker','darth.son@email.com');

INSERT INTO books (name, id_author) VALUES
    ('Don Quijote',1),
    ('La Divina Comedia',2),
    ('Vagabond 1-3',3),
    ('Dragon Ball 1',4);

INSERT INTO books (name) VALUES
    ('The Book of the 5 Rings');

INSERT INTO states (state) VALUES
    ('Returned'),
    ('On time'),
    ('Overdue');

INSERT INTO rents (id_customer, id_book, id_state) VALUES
    (1,2,1),
    (2,2,1),
    (1,1,2),
    (3,1,2),
    (2,2,3);

--[11:03:47 PM][vscode-sqlite][ERROR] RIGHT and FULL OUTER JOINs are not currently supported

--Obtenga todos los libros y sus autores
SELECT books.name, authors.name FROM books AS books LEFT JOIN authors AS authors ON books.id_author = authors.id;

--Obtenga todos los libros que no tienen autor
SELECT name, id_author FROM books WHERE id_author ISNULL;

--Obtenga todos los autores que no tienen libros
SELECT authors.name FROM authors AS authors LEFT JOIN books AS books ON authors.id = books.id_author WHERE books.id_author ISNULL;

--Obtenga todos los libros que han sido rentados en algún momento
SELECT books.name FROM rents AS rents LEFT JOIN books AS books ON rents.id_book = books.id GROUP BY books.name;

--Obtenga todos los libros que nunca han sido rentados
SELECT books.name FROM books as books LEFT JOIN rents as rents ON books.id = rents.id_book WHERE rents.id ISNULL;

--Obtenga todos los clientes que nunca han rentado un libro
SELECT customers.name FROM customers AS customers LEFT JOIN rents AS rents ON rents.id_customer = customers.id WHERE rents.id ISNULL;

--Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT books.name, rents.id_state FROM rents AS rents LEFT JOIN books AS books ON rents.id_book = books.id WHERE rents.id_state = 3;