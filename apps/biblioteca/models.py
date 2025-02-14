from django.db import models
import datetime


class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    website = models.URLField(max_length=30)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    email = models.EmailField(blank=True, verbose_name="e-mail")

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = "Autores"

    def __str__(self):
        return '%s %s' % (self.apellidos, self.nombre)

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField(default=datetime.date.today, blank=True)
    portada = models.ImageField(upload_to="portada", default='default.jpg', blank=True)

    def __str__(self):
        return self.titulo