from django.db import models


class Centro(models.Model):
    nombre = models.CharField(max_length=64)
    imagen = models.ImageField(upload_to='media', null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)


class Grado(models.Model):
    nombre = models.TextField()
    imagen = models.ImageField(upload_to='media', null=True, blank=True)
    centro = models.ManyToManyField(Centro)
    fecha = models.DateTimeField(auto_now_add=True)


class Asignatura(models.Model):
    nombre = models.CharField(max_length=500)
    curso = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)


class Profesor(models.Model):
    nombre = models.CharField(max_length=500)
    asignaturas = models.ManyToManyField(
        Asignatura,
        through='ProfesorAsignatura',
        through_fields=('profesor', 'asignatura')
    )
    fecha = models.DateTimeField(auto_now_add=True)


class Valoraciones(models.Model):
    nick = models.CharField(max_length=500)
    comentario = models.TextField(max_length=500)
    puntuacion = models.IntegerField()
    reportado = models.BooleanField()
    fecha = models.DateTimeField(auto_now_add=True)


class ProfesorAsignatura(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    teoria = models.BooleanField(null=True)
    practicas = models.BooleanField(null=True)
    fecha = models.DateTimeField(auto_now_add=True)
