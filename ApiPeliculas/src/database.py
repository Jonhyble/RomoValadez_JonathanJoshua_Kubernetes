from peewee import *
import hashlib

database = PostgresqlDatabase('First-Video',
                            user = 'postgres',
                            password = 'admin',
                            host = 'localhost',
                            port = 5432)


class Administrador(Model):
    IDAdmin = AutoField()
    NombreAdmin = CharField(max_length = 30)
    ApellidoP = CharField(max_length = 15)
    ApellidoM = CharField(max_length = 15, null = True)
    Usuario = CharField(max_length = 15, unique = True)
    Contrasena = CharField(max_length = 20)
    
    def __str__(self):
        return self.IDAdmin

    class Meta:
        database = database
        table_name = 'Administrador'

class Pelicula(Model):
    IDPelicula = AutoField()
    Nombre = CharField(max_length = 40)
    Descripcion = TextField()
    Director = CharField(max_length = 40)
    ClasificacionEdad = SmallIntegerField()
    Enlace = TextField()
    NombreSerie = CharField(max_length = 40, null = True)
    PeliculaActivada = BooleanField()
    
    def __str__(self):
        return self.IDPelicula

    class Meta:
        database = database
        table_name = 'Pelicula'

class Usuario(Model):
    IDUsuario = AutoField()
    NombreUsuario = CharField(max_length = 15, unique = True)
    Contrasena = CharField(max_length = 20)
    
    def __str__(self):
        return self.IDUsuario

    class Meta:
        database = database
        table_name = 'Usuario'

class Generos(Model):
    Nombre = CharField(max_length = 20, unique = True, primary_key = True)
    
    def __str__(self):
        return self.Nombre

    class Meta:
        database = database
        table_name = 'Generos'

class Usuario_Pelicula(Model):
    IDUsuario = ForeignKeyField(Usuario, backref='usuarios', db_column = 'IDUsuario')
    IDPelicula = ForeignKeyField(Pelicula, backref='peliculas', db_column = 'IDPelicula')

    def __str__(self):
        return self.IDUsuario

    class Meta:
        database = database
        table_name = 'Usuario_Pelicula'
        primary_key = CompositeKey('IDUsuario', 'IDPelicula')

class Administrador_Pelicula(Model):
    IDAdmin = ForeignKeyField(Administrador, backref='administradores', db_column = 'IDAdmin')
    IDPelicula = ForeignKeyField(Pelicula, backref='peliculas', db_column = 'IDPelicula')
    Fecha_y_Hora = DateTimeField()

    def __str__(self):
        return self.IDPelicula

    class Meta:
        database = database
        table_name = 'Administrador_Pelicula'
        primary_key = CompositeKey('IDAdmin', 'IDPelicula', 'Fecha_y_Hora')

class Genero_Pelicula(Model):
    Nombre = ForeignKeyField(Generos, backref='genero', db_column = 'Nombre')
    IDPelicula = ForeignKeyField(Pelicula, backref='peliculas', db_column = 'IDPelicula')

    def __str__(self):
        return self.IDPelicula

    class Meta:
        database = database
        table_name = 'Genero_Pelicula'
        primary_key = CompositeKey('Nombre', 'IDPelicula')