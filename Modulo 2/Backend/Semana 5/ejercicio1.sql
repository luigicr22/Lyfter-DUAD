CREATE SCHEMA lyfter_transacciones
    AUTHORIZATION postgres;

CREATE TABLE lyfter_transacciones.productos
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    name character varying(30) NOT NULL,
    stock integer NOT NULL,
    price integer NOT NULL,
    timestamp_stock timestamp NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE lyfter_transacciones.usuarios
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    name character varying(30) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE lyfter_transacciones.facturas
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    usuarios_id integer NOT NULL,
    total integer NOT NULL,
    status character varying(30) NOT NULL DEFAULT 'Pendiente',
    PRIMARY KEY (id),
    CONSTRAINT usuarios_id FOREIGN KEY (usuarios_id)
        REFERENCES lyfter_transacciones.usuarios (id)
);

CREATE TABLE lyfter_transacciones.factura_items
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    facturas_id integer NOT NULL,
    producto_id integer NOT NULL,
    quantity integer NOT NULL,
    price integer NOT NULL,
    status character varying(30) NOT NULL DEFAULT 'Pendiente',
    PRIMARY KEY (id),
    CONSTRAINT producto_id FOREIGN KEY (producto_id)
        REFERENCES lyfter_transacciones.productos (id),
    CONSTRAINT facturas_id FOREIGN KEY (facturas_id)
        REFERENCES lyfter_transacciones.facturas (id)
);

INSERT INTO lyfter_transacciones.usuarios (name)
VALUES 
    ('Alejandro Rodriguez'),
    ('Beatriz Lopez'),
    ('Carlos Mendoza'),
    ('Diana Guier'),
    ('Esteban Soto');

INSERT INTO lyfter_transacciones.productos (name, stock, price, timestamp_stock)
VALUES 
    ('Teclado Mecánico RGB', 50, 85, NOW()),
    ('Mouse Ergonómico', 120, 45, NOW()),
    ('Monitor 24" Full HD', 30, 150, NOW()),
    ('Cable HDMI 2.1', 200, 15, NOW()),
    ('Soporte para Laptop', 15, 35, NOW());

INSERT INTO lyfter_transacciones.productos (name, stock, price, timestamp_stock)
VALUES 
    ('Teclado Mecánico RGB', 50, 85, NOW()),
    ('Mouse Ergonómico', 120, 45, NOW()),
    ('Monitor 24" Full HD', 30, 150, NOW()),
    ('Cable HDMI 2.1', 200, 15, NOW()),
    ('Soporte para Laptop', 15, 35, NOW());