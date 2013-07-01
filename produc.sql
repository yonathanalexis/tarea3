BEGIN TRANSACTION;
CREATE TABLE marcas (id_marca integer PRIMARY KEY autoincrement, 
                                    nombre text, 
                                    descripcion text, 
                                    pais text);
INSERT INTO marcas VALUES(1,'Nike','Deporte','China');
INSERT INTO marcas VALUES(2,'Reebok','Deporte','Corea');
INSERT INTO marcas VALUES(3,'Samsung','Tecnologia','Japon');
INSERT INTO marcas VALUES(4,'Apple','Tecnologia','USA');
INSERT INTO marcas VALUES(5,'Microsoft','Tecnologia','USA');
CREATE TABLE productos (codigo text PRIMARY KEY, 
					nombre text,
					descripcion text, 
					color text, 
					precio integer, 
					fk_id_marca integer, 
					FOREIGN KEY (fk_id_marca) references marcas (id_marca));
INSERT INTO productos VALUES(001,'Zapatilla1','Deportivo','Morado/Rosado',1990,1);
INSERT INTO productos VALUES(002,'Zapatilla2','Deportivo','Fucsia/Rosado',2990,2);
INSERT INTO productos VALUES(003,'Buzo','Formal','Naranjo',19990,1);
INSERT INTO productos VALUES(004,'Poleron','Gala','Esmeralda',5990,2);
INSERT INTO productos VALUES(005,'Pantalon','Deportivo','Negro',8990,1);
INSERT INTO productos VALUES(006,'Galazy','Tecnologia','Negro',150000,3);
INSERT INTO productos VALUES(007,'Galazy II','Tecnologia','Negro',180000,3);
INSERT INTO productos VALUES(008,'iPhone','Tecnologia','Verde',200000,4);
INSERT INTO productos VALUES(009,'iPad','Tecnologia','Rosado',250000,4);
INSERT INTO productos VALUES(010,'Notebook','Tecnologia','Blanco',360000,3);
INSERT INTO productos VALUES(011,'Windows 95','Tecnologia','Salmon',1000,5);
INSERT INTO productos VALUES(012,'Windows Vista','Tecnologia','Refrigerador',100,5);
INSERT INTO productos VALUES(013,'Windows NT','Tecnologia','MicroOndas',100,5);
INSERT INTO productos VALUES(014,'Calcetin','Deportivo','Blanco',1450,1);
INSERT INTO productos VALUES(015,'Calcetin','Deportivo','Blanco',1350,2);
INSERT INTO productos VALUES(016,'Calzon de Lana','Deportivo','Oveja',4000,1);
INSERT INTO productos VALUES(017,'iPad 2','Tecnologia','Negro',800000,4);
INSERT INTO productos VALUES(018,'Ultrabook','Tecnologia','Plata',600000,3);
INSERT INTO productos VALUES(019,'PoleraMon','Deportivo','Azul',2500,2);
INSERT INTO productos VALUES(020,'DigiPolera','Deportivo','Rojo',3500,1);
CREATE TABLE sqlite_sequence(name,seq);
INSERT INTO sqlite_sequence VALUES('marcas',5);
COMMIT;
