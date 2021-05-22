from django.db import models
from django.urls import reverse


class Centro(models.Model):
    nombre = models.CharField(max_length=64)
    imagen = models.ImageField(upload_to='media', null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('centro-detail', kwargs={'pk': self.pk})


class Grado(models.Model):
    nombre = models.TextField()
    imagen = models.ImageField(upload_to='media', null=True, blank=True)
    centro = models.ManyToManyField(Centro)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    nombre = models.CharField(max_length=500)
    curso = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    grado=models.ManyToManyField(Grado,verbose_name="Grados en los que se imparte")

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    nombre = models.CharField(max_length=500)
    asignaturas = models.ManyToManyField(
        Asignatura,
        through='ProfesorAsignatura',
        through_fields=('profesor', 'asignatura')
    )
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
    
    def __str__(self):
        return self.nombre


class ValoracionProfesor(models.Model):
    nick = models.CharField(max_length=500)
    comentario = models.TextField(max_length=500)
    puntuacion = models.IntegerField()
    reportado = models.BooleanField()
    fecha = models.DateTimeField(auto_now_add=True)
    profesor = models.ForeignKey(
        Profesor, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Valoración-Profesor'
        verbose_name_plural = 'Valoraciones-Profesores'


class ValoracionAsignatura(models.Model):
    nick = models.CharField(max_length=500)
    comentario = models.TextField(max_length=500)
    puntuacion = models.IntegerField()
    reportado = models.BooleanField()
    fecha = models.DateTimeField(auto_now_add=True)
    asignatura = models.ForeignKey(
        Asignatura, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Valoración-Asignatura'
        verbose_name_plural = 'Valoraciones-Asignaturas'


class ProfesorAsignatura(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    teoria = models.BooleanField(null=True)
    practicas = models.BooleanField(null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profesor+"-"+self.asignatura

    class Meta:
        verbose_name = 'Profesor-Asignatura'
        verbose_name_plural = 'Profesores-Asignaturas'