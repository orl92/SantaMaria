from django.db import models


# Create your models here.
class Categoria(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.name


class Instalacion(models.Model):
    name = models.CharField(unique=True, max_length=50, verbose_name="Nombre de la Instalación")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoría')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Instalación'
        verbose_name_plural = 'Instalaciones'


class Imagen(models.Model):
    img = models.ImageField(upload_to="img")
    instalacion = models.ForeignKey(Instalacion, on_delete=models.CASCADE, verbose_name="Instalación")

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'
