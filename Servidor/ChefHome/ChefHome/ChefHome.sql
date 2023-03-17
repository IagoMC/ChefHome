CREATE DATABASE ChefHome;
USE ChefHome;

CREATE TABLE Usuarios (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(20) NOT NULL UNIQUE,
    Email VARCHAR(30) NOT NULL UNIQUE,
    Contraseña VARCHAR(50) NOT NULL,
    Descripcion VARCHAR(400) NULL,
    FotoPerfil VARCHAR(100) NULL,
    Token VARCHAR(300)
);

CREATE TABLE Publicacion (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    idCreador INT NOT NULL,
    Nombre VARCHAR(20) NOT NULL UNIQUE,
    Descripcion VARCHAR(400) NOT NULL,
    Pasos VARCHAR(800) NOT NULL,
    fecha DATE,
    Tipo VARCHAR(20) NOT NULL
);

CREATE TABLE Comentarios (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    idPublicacion INT NOT NULL,
    idUsuario INT NOT NULL,
    Comentarios VARCHAR(300) NOT NULL,
    Valoracion INT NULL
);

CREATE TABLE FotosPublicacion (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    idPublicacion INT NOT NULL,
    fotos VARCHAR(100)
);

CREATE TABLE PlatoIngredientes (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    idPublicacion INT NOT NULL,
    ingrediente VARCHAR(30) NULL
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

INSERT INTO Usuarios (Nombre, Email, Contraseña) VALUES ('Iago', 'im@gmail.com', '1234');
INSERT INTO Publicacion (idCreador, Nombre, Descripcion, Pasos, Tipo) VALUES (1, 'Ron-Cola', 'Cubata ron cola', 'Pillas un vaso y le ehcas un poco de ron y una lata de cocacola', 'Bebidas');