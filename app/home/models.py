from django.db import models


class Restaurante(models.Model):
    name = models.CharField(unique=True, max_length=50, verbose_name="Nombre")


class Hotel(models.Model):
    name = models.CharField(unique=True, max_length=50, verbose_name="Nombre")


class Transporte(models.Model):
    name = models.CharField(unique=True, max_length=50, verbose_name="Nombre")


# Create your models here.
class ReservaRestaurante(models.Model):
    restaurante = models.ForeignKey(Restaurante,  on_delete=models.CASCADE, verbose_name="Restaurante")
    num_movil = models.IntegerField(unique=True, verbose_name="Nombre de la Instalación")
    cant_personas = models.IntegerField()
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()
    fecha = models.DateField()
    mensaje = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = 'Gastronomía'
        verbose_name_plural = 'Gastronómicas'


class ReservaHotel(models.Model):
    hotel = models.ForeignKey(Hotel,  on_delete=models.CASCADE, verbose_name="Hotel")
    num_movil = models.IntegerField(unique=True, verbose_name="Nombre de la Instalación")
    cant_mayores = models.IntegerField()
    cant_menores = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    cant_habitaciones = models.IntegerField()
    mensaje = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = 'Alojamiento'
        verbose_name_plural = 'Alojamientos'


class ReservaTransporte(models.Model):
    transporte = models.ForeignKey(Transporte,  on_delete=models.CASCADE, verbose_name="Transporte")
    num_movil = models.IntegerField(unique=True, verbose_name="Nombre de la Instalación")
    cant_personas = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
    cant_bici = models.IntegerField()
    mensaje = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = 'Transporte'
        verbose_name_plural = 'Transportes'
