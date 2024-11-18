from django.db import models

class Marca(models.Model):
    mar_nombre = models.CharField(max_length=45)

class Modelo(models.Model):
    mod_nombre = models.CharField(max_length=45)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

class Version(models.Model):
    ver_nombre = models.CharField(max_length=45)
    ver_potencia = models.CharField(max_length=45)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

class Vehiculo(models.Model):
    veh_matricula = models.CharField(max_length=20)
    veh_color = models.CharField(max_length=20)
    veh_tipo = models.CharField(max_length=20)
    veh_garantia = models.IntegerField()
    version = models.ForeignKey(Version, on_delete=models.CASCADE)

class Cliente(models.Model):
    cli_identificacion = models.CharField(max_length=45)
    cli_nombre = models.CharField(max_length=100)
    cli_apellido = models.CharField(max_length=100)
    cli_direccion = models.CharField(max_length=80)
    cli_telefono = models.CharField(max_length=10)

class Vendedor(models.Model):
    ven_identificacion = models.CharField(max_length=45)
    ven_nombre = models.CharField(max_length=100)
    ven_apellido = models.CharField(max_length=100)
    ven_direccion = models.CharField(max_length=80)
    ven_telefono = models.CharField(max_length=10)

class Pais(models.Model):
    pai_nombre = models.CharField(max_length=45)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

class Venta(models.Model):
    vent_fechaventa = models.DateField()
    vent_precio_final = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
