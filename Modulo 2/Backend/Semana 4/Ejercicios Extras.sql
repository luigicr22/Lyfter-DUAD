--1. Explicación cruzada entre conjuntos y SQL
Analice la operación de conjuntos All - Odd.
Explique cómo una operación similar se puede representar en SQL con JOINs.
¿Qué tipo de JOIN usaría?
Las operaraciones JOINs devuelven una tabla con todas las relaciones de coincidencia.
Al hacer una operacion JOIN entre ALL y Odd se va a colocar un NULL para los numeros que no coinciden en alguna de las tablas, que son justamente los que andamos buscando.
Entonce si utilizamos un LEFT JOIN, con ALL a la izquierda, seguido de un WHERE donde seleccionamos todos los NULL de la tabla de la derecha, obtenemos los numeros de la operación de conjuntos All - Odd.


2. Agrupamiento y conteo cruzado
Usando las tablas de Books, Customers y Rents:
Obtenga el número total de veces que cada cliente ha rentado un libro
SELECT customers.name, count(*) AS veces_rentado FROM customers AS customers LEFT JOIN rents AS rents ON rents.id_customer = customers.id GROUP BY customers.name;

Ordene de mayor a menor y limite el resultado a los 3 clientes más activos
SELECT customers.name, count(*) AS veces_rentado FROM customers AS customers LEFT JOIN rents AS rents ON rents.id_customer = customers.id GROUP BY customers.name ORDER BY veces_rentado DESC Limit 3;

Debe usar: GROUP BY, COUNT(), ORDER BY, LIMIT

3. Consulta con múltiples JOINS anidados
Genere un SELECT que devuelva lo siguiente:
Nombre del cliente
Nombre del libro
Nombre del autor
Estado del alquiler (Rents.State)
Debe manejar el caso en que un libro no tenga autor

SELECT customers.name AS Customer, books.name AS Book, authors.name AS Author, states.state AS State FROM rents as rents 
INNER JOIN customers AS customers ON customers.id = rents.id_customer
INNER JOIN states AS states ON states.id = rents.id_state
INNER JOIN books AS books ON rents.id_book = books.id
LEFT JOIN authors AS authors ON books.id_author = authors.id;