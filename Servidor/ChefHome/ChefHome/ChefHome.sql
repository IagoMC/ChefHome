CREATE DATABASE ChefHome;
USE ChefHome;

CREATE TABLE Usuarios (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(30) NOT NULL UNIQUE,
    contraseña VARCHAR(300) NOT NULL,
    descripcion VARCHAR(600) NULL,
    fotoPerfil VARCHAR(300) NULL,
    token VARCHAR(300)
);

CREATE TABLE Publicacion (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    idCreador INT NOT NULL,
    nombre VARCHAR(20) NOT NULL UNIQUE,
    descripcion VARCHAR(600) NOT NULL,
    pasos VARCHAR(3000) NOT NULL,
    fecha DATE,
    tipo VARCHAR(20) NOT NULL
);

CREATE TABLE Comentarios (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    idPublicacion INT NOT NULL,
    idUsuario INT NOT NULL,
    comentarios VARCHAR(300) NOT NULL,
    valoracion INT NULL
);

CREATE TABLE FotosPublicacion (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    idPublicacion INT NOT NULL,
    fotos VARCHAR(300)
);

CREATE TABLE PlatoIngredientes (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    idPublicacion INT NOT NULL,
    ingrediente VARCHAR(100) NULL
);

CREATE TABLE Seguidores (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    idUsuario INT NOT NULL,
    idSeguido INT NOT NULL,
    CONSTRAINT fk_idusuario FOREIGN KEY (idUsuario) REFERENCES Usuarios (id),
    CONSTRAINT fk_idseguido FOREIGN KEY (idSeguido) REFERENCES Usuarios (id)
);

/*Foreign key*/
ALTER TABLE Comentarios ADD FOREIGN KEY (idPublicacion) REFERENCES Publicacion (id);
ALTER TABLE Comentarios ADD FOREIGN KEY (idUsuario) REFERENCES Usuarios (id);
ALTER TABLE FotosPublicacion ADD FOREIGN KEY (idPublicacion) REFERENCES Publicacion (id);
ALTER TABLE PlatoIngredientes ADD FOREIGN KEY (idPublicacion) REFERENCES Publicacion (id);
ALTER TABLE Publicacion ADD FOREIGN KEY (idCreador) REFERENCES Usuarios (id);

INSERT INTO Usuarios (nombre, email, contraseña) VALUES ('Iago', 'im@gmail.com', '1234');
INSERT INTO Publicacion (idCreador, nombre, descripcion, pasos, tipo) VALUES (1, 'Ron-Cola', 'Cubata ron cola', 'Pillas un vaso y le ehcas un poco de ron y una lata de cocacola', 'Bebidas');