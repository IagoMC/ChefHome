# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comentarios(models.Model):
    idpublicacion = models.ForeignKey('Publicacion', models.DO_NOTHING, db_column='idPublicacion')  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    comentarios = models.CharField(db_column='Comentarios', max_length=300)  # Field name made lowercase.
    valoracion = models.IntegerField(db_column='Valoracion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comentarios'


class Fotospublicacion(models.Model):
    idpublicacion = models.ForeignKey('Publicacion', models.DO_NOTHING, db_column='idPublicacion')  # Field name made lowercase.
    fotos = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FotosPublicacion'


class Platoingredientes(models.Model):
    idpublicacion = models.ForeignKey('Publicacion', models.DO_NOTHING, db_column='idPublicacion')  # Field name made lowercase.
    ingrediente = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlatoIngredientes'


class Publicacion(models.Model):
    idcreador = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idCreador')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=400)  # Field name made lowercase.
    pasos = models.CharField(db_column='Pasos', max_length=800)  # Field name made lowercase.
    fecha = models.DateField(blank=True, null=True)
    tipo = models.CharField(db_column='Tipo', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Publicacion'


class Seguidores(models.Model):
    id = models.IntegerField(primary_key=True)
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    idseguido = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idSeguido')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Seguidores'


class Usuarios(models.Model):
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=30)  # Field name made lowercase.
    contraseña = models.CharField(db_column='Contraseña', max_length=50)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=400, blank=True, null=True)  # Field name made lowercase.
    fotoperfil = models.CharField(db_column='FotoPerfil', max_length=100, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(db_column='Token', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuarios'
