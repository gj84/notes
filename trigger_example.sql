create table 'producto' (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'nombre' CHAR(50) NOT NULL,
    'precio' REAL NOT NULL
);

create table 'stock' (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'producto' INTEGER REFERENCES 'producto' ('id'),
    'cantidad' INTEGER
);

create table 'ventas' (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'producto' INTEGER REFERENCES 'producto' ('id'),
    'cantidad' INTEGER,
    'fechahora' DATETIME
);


create trigger 'restar_stock' after insert on ventas 
    BEGIN
        UPDATE stock SET cantidad = cantidad - new.cantidad where stock.producto = new.producto;
    END;

insert into producto (nombre, precio) values ('detergente', 16);
insert into producto (nombre, precio) values ('lavandina', 10);
insert into producto (nombre, precio) values ('jabon', 6);
insert into producto (nombre, precio) values ('dentrifico', 26);
insert into producto (nombre, precio) values ('esponja', 4.5);
insert into producto (nombre, precio) values ('suavizante', 18.3);

select * from producto;

insert into stock (producto, cantidad) values (1, 100);
insert into stock (producto, cantidad) values (2, 100);
insert into stock (producto, cantidad) values (3, 70);
insert into stock (producto, cantidad) values (4, 50);
insert into stock (producto, cantidad) values (5, 40);
insert into stock (producto, cantidad) values (6, 90);

select id, producto.nombre, cantidad from stock inner join producto on stock.producto=producto.id;

insert into ventas (producto, cantidad, fechahora) values (2, 37, datetime('now'));

select * from ventas;
select id, producto.nombre, cantidad from stock inner join producto on stock.producto=producto.id;
