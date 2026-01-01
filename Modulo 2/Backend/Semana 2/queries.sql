-- Ejercicios de SQL
--1)Cree una nueva base de datos en SQLite.
    --db_ejercicios.db

--2) Replique las tablas creadas anteriormente en Ejercicios de Bases de Datos, con sus respectivos PKs, FKs, constraints, y demás requerimientos.
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(25) NOT NULL,
    email VARCHAR(25) UNIQUE NOT NULL,
    registration_date TIMESTAMP NOT NULL
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(10) UNIQUE NOT NULL,
    name VARCHAR(25) NOT NULL,
    price INTEGER NOT NULL,
    entry_date TIMESTAMP NOT NULL,
    brand VARCHAR(25) NOT NULL
);

CREATE TABLE payment_methods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type VARCHAR(25) NOT NULL,
    bank VARCHAR(25) NOT NULL
);

CREATE TABLE invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number INTEGER UNIQUE NOT NULL,
    purchase_date TIMESTAMP NOT NULL,
    id_user INTEGER NOT NULL REFERENCES users(id),
    total_amount INTEGER NOT NULL,
    id_payment_method INTEGER NOT NULL REFERENCES payment_methods(id)
);

CREATE TABLE invoice_product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_product INTEGER NOT NULL REFERENCES products(id),
    id_invoice INTEGER NOT NULL REFERENCES invoices(id),
    quantity SMALLINT NOT NULL,
    total_amount INTEGER NOT NULL
);

CREATE TABLE product_reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_product INTEGER NOT NULL REFERENCES products(id),
    id_user INTEGER NOT NULL REFERENCES users(id),
    comment text NOT NULL,
    score SMALLINT NOT NULL,
    date_review TIMESTAMP NOT NULL
);

CREATE TABLE shopping_cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_product INTEGER NOT NULL REFERENCES products(id),
    id_user INTEGER NOT NULL REFERENCES users(id),
    quantity SMALLINT NOT NULL
);

--3)Modifique la tabla de Facturas creada en el ejercicio anterior y agregue una columna para almacenar también el número de teléfono del comprador, y otra para el código de empleado del cajero que realizó la venta.
--EJERCICIO EXTRA 3. Agregue a invoices las columnas phone (TEXT, puede ser NULL) y cashier_code (TEXT, por defecto 'N/A')

ALTER TABLE invoices
    ADD phone TEXT;

ALTER TABLE invoices
    ADD cashier_code TEXT NOT NULL DEFAULT 'N/A';


--inserts para pruebas
INSERT INTO users (name, email, registration_date)
    VALUES
    ('Juan Pérez', 'juan@example.com', '2025-01-10 09:30:00'),
    ('Ana Gómez', 'ana@example.com', '2025-02-15 14:20:00'),
    ('Carlos Ruiz', 'carlos@example.com', '2025-03-05 18:45:00'),
    ('Laura Méndez', 'laura@example.com', '2025-03-10 10:00:00'),
    ('Pedro Sánchez', 'pedro@example.com', '2025-03-12 11:15:00'),
    ('María López', 'maria@example.com', '2025-03-14 12:30:00'),
    ('Luis Torres', 'luis@example.com', '2025-03-16 13:45:00'),
    ('Sofía Vargas', 'sofia@example.com', '2025-03-18 15:00:00'),
    ('Andrés Castro', 'andres@example.com', '2025-03-20 16:15:00'),
    ('Valeria Rojas', 'valeria@example.com', '2025-03-22 17:30:00');

INSERT INTO products (code, name, price, entry_date, brand)
    VALUES
        ('P001', 'Laptop', 850000, '2025-02-01 10:00:00', 'Dell'),
        ('P002', 'Smartphone', 450000, '2025-02-10 11:30:00', 'Samsung'),
        ('P003', 'Auriculares', 35000, '2025-03-01 09:15:00', 'Sony'),
        ('P004', 'Tablet', 300000, '2025-03-05 14:00:00', 'Apple'),
        ('P005', 'Monitor', 150000, '2025-03-07 15:30:00', 'LG'),
        ('P006', 'Teclado', 25000, '2025-03-09 16:45:00', 'Logitech'),
        ('P007', 'Mouse', 15000, '2025-03-11 17:00:00', 'Logitech'),
        ('P008', 'Impresora', 120000, '2025-03-13 18:15:00', 'HP'),
        ('P009', 'Cámara Web', 40000, '2025-03-15 19:30:00', 'Microsoft'),
        ('P010', 'Disco SSD', 95000, '2025-03-17 20:45:00', 'Kingston');

INSERT INTO payment_methods (type, bank)
    VALUES
        ('Tarjeta Crédito', 'BAC'),
        ('Transferencia', 'BN'),
        ('Efectivo', 'Caja'),
        ('PayPal', 'Online'),
        ('Tarjeta Débito', 'BAC'),
        ('Cheque', 'Caja'),
        ('Criptomoneda', 'Wallet'),
        ('Pago Móvil', 'BN'),
        ('Stripe', 'Online'),
        ('Apple Pay', 'Apple');

INSERT INTO invoices (invoice_number, purchase_date, id_user, total_amount, id_payment_method)
    VALUES
        (1001, '2025-03-10 12:00:00', 1, 885000, 1),
        (1002, '2025-03-12 15:30:00', 2, 450000, 2),
        (1003, '2025-03-15 17:45:00', 3, 35000, 3),
        (1004, '2025-03-16 10:20:00', 4, 300000, 4),
        (1005, '2025-03-17 11:30:00', 5, 150000, 5),
        (1006, '2025-03-18 12:40:00', 6, 25000, 6),
        (1007, '2025-03-19 13:50:00', 7, 15000, 7),
        (1008, '2025-03-20 14:00:00', 8, 120000, 8),
        (1009, '2025-03-21 15:10:00', 9, 40000, 9),
        (1010, '2025-03-22 16:20:00', 10, 95000, 10);

INSERT INTO invoice_product (id_product, id_invoice, quantity, total_amount)
    VALUES
        (1, 1, 1, 850000),
        (3, 1, 1, 35000),
        (2, 2, 1, 450000),
        (3, 3, 1, 35000),
        (4, 4, 1, 300000),
        (5, 5, 1, 150000),
        (6, 6, 1, 25000),
        (7, 7, 1, 15000),
        (8, 8, 1, 120000),
        (9, 9, 1, 40000);

INSERT INTO product_reviews (id_product, id_user, comment, score, date_review)
    VALUES
        (1, 1, 'Excelente rendimiento', 5, '2025-03-20 10:00:00'),
        (2, 2, 'Muy buena cámara', 4, '2025-03-21 11:15:00'),
        (3, 3, 'Sonido aceptable', 3, '2025-03-22 09:45:00'),
        (4, 4, 'Pantalla brillante', 5, '2025-03-23 10:30:00'),
        (5, 5, 'Buen tamaño', 4, '2025-03-24 11:00:00'),
        (6, 6, 'Teclas cómodas', 4, '2025-03-25 12:15:00'),
        (7, 7, 'Buen diseño', 4, '2025-03-26 13:20:00'),
        (8, 8, 'Impresión rápida', 5, '2025-03-27 14:30:00'),
        (9, 9, 'Buena calidad de imagen', 4, '2025-03-28 15:45:00'),
        (10, 10, 'Velocidad excelente', 5, '2025-03-29 16:50:00');


INSERT INTO shopping_cart (id_product, id_user, quantity)
    VALUES
        (2, 1, 1),
        (3, 2, 2),
        (1, 3, 1),
        (4, 4, 1),
        (5, 5, 1),
        (6, 6, 3),
        (7, 7, 2),
        (8, 8, 1),
        (9, 9, 1),
        (10, 10, 1);


--4)Realice los siguientes SELECT:
    --1)Obtenga todos los productos almacenados
    SELECT * FROM products;

    --2)Obtenga todos los productos que tengan un precio mayor a 50000
    SELECT * FROM products WHERE price > 50000;

    --3)Obtenga todas las compras de un mismo producto por id.
    SELECT id_product, id_invoice FROM invoice_product WHERE id_product = 3;

    --4)Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
    SELECT id_product, SUM(total_amount) FROM invoice_product GROUP BY id_product;

    --5)Obtenga todas las facturas realizadas por el mismo comprador
    SELECT id_user, invoice_number FROM invoices WHERE id_user = 1;

    --6)Obtenga todas las facturas ordenadas por monto total de forma descendente
    SELECT invoice_number, total_amount FROM invoices ORDER BY total_amount DESC;

    --7)Obtenga una sola factura por número de factura.
    SELECT * FROM invoices WHERE invoice_number = '1006';
    --invoice_number esta creada como unique por lo que solo existe una.


--Ejercicios extra de SQL
--1. Crear categorías y ajustar productos
    --Cree la tabla categories con: id (PK autoincrement), name (UNIQUE, NOT NULL), description
    CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) UNIQUE NOT NULL,
    description text NOT NULL
    );
    --Agregue a products la columna category_id (INTEGER, puede permitir NULL)
    ALTER TABLE products
    ADD id_category INTEGER REFERENCES categories(id);

    --Se agrega adicionalmente a products la columna quantity (INTEGER NOT NULL DEFAULT 0), ya que se utiliza mas adelante. 
    ALTER TABLE products
    ADD quantity INTEGER NOT NULL DEFAULT 0;

    --Inserte al menos 3 filas en categories
    INSERT INTO categories (name, description)
    VALUES
        ('Electrónica', 'Dispositivos electrónicos como laptops, smartphones y tablets'),
        ('Accesorios', 'Complementos para equipos de cómputo como teclados, mouse y auriculares'),
        ('Periféricos', 'Monitores, impresoras y dispositivos de almacenamiento');


    --Actualice algunos products asignándoles un category_id
    UPDATE products SET id_category = 1 WHERE id = 1;
    UPDATE products SET id_category = 2 WHERE id = 3;
    UPDATE products SET id_category = 3 WHERE id = 5;   

    --Verifique con SELECT * FROM products (muestre id, product_name, price, quantity, category_id)
    SELECT id, name, price, quantity, id_category FROM products;

--2. Carga de productos y filtros básicos
    --Inserte al menos 10 filas en products con product_name, price, quantity
        --realizado previamente en inserts para pruebas.
        --Se actualiza el valor de quantity.
            UPDATE products SET quantity = 10 WHERE id = 1;
            UPDATE products SET quantity = 15 WHERE id = 2;
            UPDATE products SET quantity = 20 WHERE id = 3;
            UPDATE products SET quantity = 25 WHERE id = 4;
            UPDATE products SET quantity = 30 WHERE id = 5;
            UPDATE products SET quantity = 35 WHERE id = 6;
            UPDATE products SET quantity = 40 WHERE id = 7;
            UPDATE products SET quantity = 45 WHERE id = 8;
            UPDATE products SET quantity = 50 WHERE id = 9;
            UPDATE products SET quantity = 55 WHERE id = 10;

    --Seleccione todos los productos
    SELECT * FROM products;

    --Seleccione productos con price > 50000
    SELECT * FROM products WHERE price > 50000;

    --Seleccione productos cuyo product_name contenga la palabra “apple” usando LIKE
    INSERT INTO products (code, name, price, entry_date, brand, id_category, quantity) VALUES
    ('P011', 'Apple AirPods', 75000, '2025-03-30 10:00:00', 'Apple', 2, 60);

    SELECT * FROM products WHERE name LIKE '%apple%';

    --Liste los 5 productos más caros con ORDER BY price DESC LIMIT 5
    SELECT * FROM products ORDER BY price DESC LIMIT 5;

--3. Campos nuevos en facturas y actualización
    --Agregue a invoices las columnas phone (TEXT, puede ser NULL) y cashier_code (TEXT, por defecto 'N/A')
        --Realizado previamente en ejercicio 3.

    --Actualice varias facturas asignando valores a phone y cashier_code
    UPDATE invoices SET phone = '8356-9524', cashier_code = 'CC-562' WHERE id = 1;
    UPDATE invoices SET phone = '8356-9684', cashier_code = 'CC-123' WHERE id = 3;
    UPDATE invoices SET phone = '7635-9524', cashier_code = 'CC-456' WHERE id = 5;
    UPDATE invoices SET phone = '8398-3224', cashier_code = 'CC-789' WHERE id = 7;
    UPDATE invoices SET phone = '8784-3204', cashier_code = 'CC-001' WHERE id = 9;

    --Seleccione todas las facturas que tengan phone vacío o NULL
    SELECT * FROM invoices WHERE phone ISNULL;

    --Seleccione una sola factura por invoice_id
    SELECT * FROM invoices WHERE id = 2;

--4. Correcciones de datos en productos
    UPDATE products SET price = 0 WHERE id = 7;
    UPDATE products SET price = -5000 WHERE id = 3;

    --Establezca quantity = 0 donde price <= 0
    UPDATE products SET quantity = 0 WHERE price <= 0;

    --Aumente el price en 100 unidades para todos los productos cuando quantity sea menor a 10
    UPDATE products SET price = (price + 100) WHERE quantity < 10;

    --Disminuya quantity en 1 para un product_id específico
    UPDATE products SET quantity = quantity - 1 WHERE id = 8;

    --Verifique con SELECT * FROM products ORDER BY id ASC LIMIT 10
    SELECT * FROM products ORDER BY id ASC LIMIT 10;