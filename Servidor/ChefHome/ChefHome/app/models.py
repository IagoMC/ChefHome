# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.hashers import check_password

class Comentarios(models.Model):
    idpublicacion = models.ForeignKey('Publicacion', models.DO_NOTHING, db_column='idPublicacion')  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    comentarios = models.CharField(max_length=300)
    valoracion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Comentarios'


class Fotospublicacion(models.Model):
    idpublicacion = models.ForeignKey('Publicacion', models.DO_NOTHING, db_column='idPublicacion')  # Field name made lowercase.
    fotos = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FotosPublicacion'


class Platoingredientes(models.Model):
    idpublicacion = models.ForeignKey('Publicacion', models.DO_NOTHING, db_column='idPublicacion')  # Field name made lowercase.
    ingrediente = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlatoIngredientes'


class Publicacion(models.Model):
    idcreador = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idCreador')  # Field name made lowercase.
    nombre = models.CharField(unique=True, max_length=20)
    descripcion = models.CharField(max_length=600)
    pasos = models.CharField(max_length=3000)
    fecha = models.DateField(blank=True, null=True)
    tipo = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'Publicacion'

"""
class Seguidores(models.Model):
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    idseguido = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idSeguido')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Seguidores'
"""
class Seguidores(models.Model):
    idseguido = models.ForeignKey('Usuarios', on_delete=models.CASCADE, related_name='seguidores_de')
    idusuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE, related_name='usuarios_seguidos')


class Usuarios(models.Model):
    nombre = models.CharField(unique=True, max_length=20)
    email = models.CharField(unique=True, max_length=30)
    contraseña = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=600, blank=True, null=True)
    fotoperfil = models.CharField(db_column='fotoPerfil', max_length=300, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(max_length=300, blank=True, null=True)

    def check_password(self, sinCifrarContrasena):
        # Compara la contraseña enviada con la de la BD
        return check_password(sinCifrarContrasena, self.contraseña)
    class Meta:
        managed = False
        db_table = 'Usuarios'
