CREATE DATABASE PROJECT_GT_FLASK;
------------no necesario, sqlalquemy ya crea las tablas  solo por documentación-------------
-- Tabla estudiantes
CREATE TABLE estudiante (
    id_estudiante SERIAL PRIMARY KEY,
    no_documento VARCHAR(30) NOT NULL,
    primer_nombre VARCHAR(100) NOT NULL,
    segundo_nombre VARCHAR(100),
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(150) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    fecha_creo TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON COLUMN estudiante.fecha_creo IS 'fecha en que se creo el registro en el sistema';
CREATE TABLE programa (
    id_programa SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(500),
    fecha_creo TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE curso (
    id_curso SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(500),
    id_programa INTEGER NOT NULL REFERENCES programa(id_programa),
    fecha_creo TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE estudiante_curso (
    id_estudiante INTEGER NOT NULL REFERENCES estudiante(id_estudiante),
    id_curso INTEGER NOT NULL REFERENCES curso(id_curso),
    nota DECIMAL(3,2),
    PRIMARY KEY (id_estudiante, id_curso),
    fecha_creo TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
--------------------------------

------------Inserts de ejemplo-------------
-- Insertar algunos programas
INSERT INTO programa (nombre, descripcion) VALUES
('Ingeniería de Sistemas', 'Programa que forma profesionales en el desarrollo de software y sistemas de información'),
('Matemáticas', 'Programa que forma profesionales en el estudio de las estructuras abstractas y sus aplicaciones'),
('Psicología', 'Programa que forma profesionales en el estudio del comportamiento humano y los procesos mentales');
INSERT INTO programa (nombre, descripcion) VALUES
('Filosofía', 'Programa que forma profesionales en el estudio de las ideas y los problemas fundamentales de la existencia humana'),
('Biología', 'Programa que forma profesionales en el estudio de los seres vivos y sus procesos vitales'),
('Arte', 'Programa que forma profesionales en el estudio y la práctica de las diversas formas de expresión artística');

-- Insertar algunos cursos
INSERT INTO curso (nombre, descripcion, id_programa) VALUES
('Algoritmos y Programación', 'Curso que introduce los conceptos básicos de la programación estructurada y orientada a objetos', 1),
('Cálculo Diferencial', 'Curso que introduce los conceptos básicos del cálculo diferencial de una variable', 2),
('Psicología General', 'Curso que introduce los conceptos básicos de la psicología como ciencia y sus principales ramas', 3);
INSERT INTO curso (nombre, descripcion, id_programa) VALUES
('Lógica', 'Curso que introduce los conceptos básicos de la lógica formal y sus aplicaciones al razonamiento', 4),
('Genética', 'Curso que introduce los conceptos básicos de la genética molecular y sus aplicaciones a la biotecnología', 5),
('Pintura', 'Curso que introduce los conceptos básicos de la pintura y sus técnicas y estilos', 6);

-- Insertar algunos estudiantes
INSERT INTO estudiante (no_documento, primer_nombre, segundo_nombre, apellido, correo, fecha_nacimiento) VALUES
('12345678', 'Juan', 'David', 'Pérez', 'juan.perez@example.com', '2000-01-01'),
('87654321', 'María', NULL, 'García', 'maria.garcia@example.com', '2001-02-02'),
('45678912', 'Carlos', 'Andrés', 'López', 'carlos.lopez@example.com', '2002-03-03');
INSERT INTO estudiante (no_documento, primer_nombre, segundo_nombre, apellido, correo, fecha_nacimiento) VALUES
('34567890', 'Ana', 'Lucía', 'Ramírez', 'ana.ramirez@example.com', '2003-04-04'),
('90123456', 'Pedro', NULL, 'Gómez', 'pedro.gomez@example.com', '2004-05-05'),
('78901234', 'Laura', NULL, 'Torres', 'laura.torres@example.com', '2005-06-06');

-- Insertar algunas relaciones entre estudiantes y cursos
INSERT INTO estudiante_curso (id_estudiante, id_curso, nota) VALUES
(1, 1, 4.5), -- Juan Pérez cursó Algoritmos y Programación con nota 4.5
(1, 2, 3.0), -- Juan Pérez cursó Cálculo Diferencial con nota 3.0
(2, 3, 4.0), -- María García cursó Psicología General con nota 4.0
(3, 1, 3.5), -- Carlos López cursó Algoritmos y Programación con nota 3.5
(3, 3, 4.2); -- Carlos López cursó Psicología General con nota 4.2
INSERT INTO estudiante_curso (id_estudiante, id_curso, nota) VALUES
(4, 4, 4.0), -- Ana Ramírez cursó Lógica con nota 4.0
(4, 6, 3.8), -- Ana Ramírez cursó Pintura con nota 3.8
(5, 5, 4.2), -- Pedro Gómez cursó Genética con nota 4.2
(6, 3, 3.5), -- Laura Torres cursó Psicología General con nota 3.5
(6, 6, 4.5); -- Laura Torres cursó Pintura con nota 4.5