SET search_path TO lyfter_car_rental;

DROP TABLE IF EXISTS Users;

CREATE TABLE Users(
	id SERIAL PRIMARY KEY,
	name VARCHAR(15) NOT NULL,
	email VARCHAR(20) NOT NULL UNIQUE,
	username VARCHAR(20) NOT NULL UNIQUE,
	password VARCHAR(15) NOT NULL,
	birth_date DATE NOT NULL,
	account_status VARCHAR(10) NOT NULL
);

INSERT INTO Users (name, email, username, password, birth_date, account_status)
VALUES
('Carlos Mora', 'carlos.m@mail.com', 'carlosmora', 'Cm123456', '1998-03-15', 'active'),
('Ana Lopez', 'ana.lopez@mail.com', 'analopez', 'Al234567', '2000-07-22', 'active'),
('Pedro Rojas', 'pedro.r@mail.com', 'pedrorojas', 'Pr345678', '1995-11-08', 'inactive'),
('Maria Soto', 'maria.soto@mail.com', 'mariasoto', 'Ms456789', '2002-01-19', 'active'),
('Luis Castro', 'luis.c@mail.com', 'luiscastro', 'Lc567890', '1997-05-30', 'active'),
('Sofia Vargas', 'sofia.v@mail.com', 'sofiavargas', 'Sv678901', '1999-09-12', 'inactive'),
('Diego Arias', 'diego.a@mail.com', 'diegoarias', 'Da789012', '2001-04-25', 'active'),
('Laura Mendez', 'laura.m@mail.com', 'lauramendez', 'Lm890123', '1996-12-03', 'active'),
('Andres Vega', 'andres.v@mail.com', 'andresvega', 'Av901234', '2003-08-17', 'inactive'),
('Paula Solis', 'paula.s@mail.com', 'paulasolis', 'Ps012345', '1994-06-09', 'active'),

('Jorge Marin', 'jorge.m@mail.com', 'jorgemarin', 'Jm112233', '1998-02-14', 'active'),
('Elena Ruiz', 'elena.r@mail.com', 'elenaruiz', 'Er223344', '2000-10-28', 'inactive'),
('Mario Diaz', 'mario.d@mail.com', 'mariodiaz', 'Md334455', '1997-07-06', 'active'),
('Valeria Leon', 'valeria.l@mail.com', 'valerialeon', 'Vl445566', '2001-03-21', 'active'),
('Oscar Campos', 'oscar.c@mail.com', 'oscarcampos', 'Oc556677', '1995-09-18', 'inactive'),
('Lucia Salas', 'lucia.s@mail.com', 'luciasalas', 'Ls667788', '1999-01-11', 'active'),
('Kevin Flores', 'kevin.f@mail.com', 'kevinflores', 'Kf778899', '2002-05-04', 'active'),
('Daniela Paz', 'daniela.p@mail.com', 'danielapaz', 'Dp889900', '1996-08-29', 'inactive'),
('Pablo Nunez', 'pablo.n@mail.com', 'pablonunez', 'Pn990011', '2003-12-16', 'active'),
('Natalia Cruz', 'natalia.c@mail.com', 'nataliacruz', 'Nc001122', '1994-04-07', 'active'),

('Ricardo Gil', 'ricardo.g@mail.com', 'ricardogil', 'Rg121212', '1998-11-23', 'inactive'),
('Camila Mora', 'camila.m@mail.com', 'camilamora', 'Cm232323', '2000-06-13', 'active'),
('Esteban Rios', 'esteban.r@mail.com', 'estebanrios', 'Er343434', '1997-02-27', 'active'),
('Gabriela Rey', 'gabriela.r@mail.com', 'gabrielarey', 'Gr454545', '2001-09-05', 'inactive'),
('Felipe Soto', 'felipe.s@mail.com', 'felipesoto', 'Fs565656', '1995-03-31', 'active'),
('Monica Lara', 'monica.l@mail.com', 'monicalara', 'Ml676767', '1999-07-14', 'active'),
('Adrian Ponce', 'adrian.p@mail.com', 'adrianponce', 'Ap787878', '2002-10-20', 'inactive'),
('Irene Bravo', 'irene.b@mail.com', 'irenebravo', 'Ib898989', '1996-01-26', 'active'),
('Samuel Ortiz', 'samuel.o@mail.com', 'samuelortiz', 'So909090', '2003-05-09', 'active'),
('Julia Acosta', 'julia.a@mail.com', 'juliaacosta', 'Ja101010', '1994-12-02', 'inactive'),

('Roberto Mena', 'roberto.m@mail.com', 'robertomena', 'Rm131313', '1998-08-18', 'active'),
('Claudia Roca', 'claudia.r@mail.com', 'claudiaroca', 'Cr242424', '2000-02-05', 'active'),
('Hector Silva', 'hector.s@mail.com', 'hectorsilva', 'Hs353535', '1997-10-11', 'inactive'),
('Patricia Gil', 'patricia.g@mail.com', 'patriciagil', 'Pg464646', '2001-06-24', 'active'),
('Alberto Leon', 'alberto.l@mail.com', 'albertoleon', 'Al575757', '1995-01-17', 'active'),
('Teresa Moya', 'teresa.m@mail.com', 'teresamoya', 'Tm686868', '1999-04-30', 'inactive'),
('Cristian Paz', 'cristian.p@mail.com', 'cristianpaz', 'Cp797979', '2002-11-07', 'active'),
('Beatriz Mora', 'beatriz.m@mail.com', 'beatrizmora', 'Bm808080', '1996-03-12', 'active'),
('Mauricio Sol', 'mauricio.s@mail.com', 'mauriciosol', 'Ms919191', '2003-07-28', 'inactive'),
('Andrea Luna', 'andrea.l@mail.com', 'andrealuna', 'Al020202', '1994-09-15', 'active'),

('Ivan Rojas', 'ivan.r@mail.com', 'ivanrojas', 'Ir141414', '1998-05-22', 'active'),
('Rosa Navarro', 'rosa.n@mail.com', 'rosanavarro', 'Rn252525', '2000-12-09', 'inactive'),
('Emilio Salas', 'emilio.s@mail.com', 'emiliosalas', 'Es363636', '1997-04-16', 'active'),
('Carolina Rey', 'carolina.r@mail.com', 'carolinarey', 'Cr474747', '2001-08-03', 'active'),
('Tomas Vega', 'tomas.v@mail.com', 'tomasvega', 'Tv585858', '1995-06-27', 'inactive'),
('Diana Castro', 'diana.c@mail.com', 'dianacastro', 'Dc696969', '1999-11-19', 'active'),
('Rafael Moya', 'rafael.m@mail.com', 'rafaelmoya', 'Rm707070', '2002-02-08', 'active'),
('Silvia Marin', 'silvia.m@mail.com', 'silviamarin', 'Sm818181', '1996-10-25', 'inactive'),
('Martin Arias', 'martin.a@mail.com', 'martinarias', 'Ma929292', '2003-03-14', 'active'),
('Isabel Rios', 'isabel.r@mail.com', 'isabelrios', 'Ir030303', '1994-07-01', 'active');