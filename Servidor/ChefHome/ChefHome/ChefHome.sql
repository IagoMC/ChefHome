create database ChefHome;
use ChefHome;
create table Usuarios(
	id int not null primary key auto_increment unique,
    Nombre varchar(20) not null unique,
    Email varchar(30) not null unique,
    Contraseña varchar(50) not null ,
	Descripcion varchar(400) null,
    FotoPerfil varchar(100) null,
    Token varchar(20) 
);

create table Publicacion (
	id int not null primary key auto_increment unique,
    idCreador int not null,
    Nombre varchar(20) not null unique,
	Descripcion varchar(400) not null,
    Pasos varchar(800) not null,
    fecha date,
	Tipo varchar(20) not null
);

create table Comentarios (
	id int not null primary key auto_increment unique,
    idPublicacion int not null,
    idUsuario int not null,
    Comentarios varchar(300) not null,
	Valoracion int null

);

Create table FotosPublicacion (
	id int not null primary key auto_increment unique,
    idPublicacion int not null,
    fotos varchar(100)
 );
 
 
create table PlatoIngredientes (
	id int not null primary key auto_increment unique,
    idPublicacion int not null,
    ingrediente varchar(30) null
  
);

create table Seguidores(
	id int not null primary key unique,
    idUsuario int not null,
    idSeguido int not null
);

/*Foreign key*/
alter table  Comentarios add foreign key(idPublicacion) references Publicacion(id);
alter table  Comentarios add foreign key(idUsuario) references Usuarios(id);
alter table  FotosPublicacion add foreign key(idPublicacion) references Publicacion(id);
alter table  PlatoIngredientes add foreign key(idPublicacion) references Publicacion(id);

alter table  Publicacion add foreign key(idCreador) references Usuarios(id);

alter table  Seguidores add foreign key(idUsuario) references Usuarios(id);
alter table  Seguidores add foreign key(idSeguido) references Usuarios(id);


insert into Usuarios (id,Nombre,Email,Contraseña) values (1,"Iago", "im@gmail.com" , "1234");
insert into Publicacion (id,idCreador,Nombre,Descripcion,Pasos,Tipo) values (1,1,"Ron-Cola", "Cubata ron cola", "Pillas un vaso y le ehcas un poco de ron y una lata de cocacola","Bebidas");