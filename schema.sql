CREATE TABLE vehiculo (
	condicion varchar(16),
	precio varchar(16),
	moneda varchar(16),
	marca varchar(16),
	modelo varchar(16),
	version varchar(16), -- ID = TRIM
	ubicacion varchar(16), -- seller_address/state/name
	year varchar(8),
	tipo_combustible varchar(16),
	transmision varchar(16), -- ID = TRANSMISSION
	kilometraje varchar(16),
	cant_puertas int,
	url_imagen varchar(256),
	url_publiation varchar(256),
	publication_title varchar(128)
);
