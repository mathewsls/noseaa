from django.db import models

class vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=50)
    fecha_fabricacion = models.DateTimeField()
    fecha_iniciar_soat = models.DateTimeField()
    fecha_final_soat = models.DateTimeField()
    is_activate = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"

class conductor(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cedula = models.IntegerField()
    correo = models.EmailField(max_length=40)
    vehiculo = models.ForeignKey(vehiculo, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField()
    is_activate = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.cedula}"

class pasajero(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cedula = models.IntegerField()
    correo = models.EmailField(max_length=50)
    tc = models.IntegerField()
    cvv = models.BooleanField()
    fecha_vencimiento = models.DateTimeField()
    fecha_inscripcion = models.DateTimeField()
    is_activate = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.cedula}"

class arrendamiento(models.Model):
    fecha = models.DateTimeField()
    zona = models.CharField(max_length=10, choices=[('norte', 'Norte'), ('sur', 'Sur'), ('oriente', 'Oriente'), ('occidente', 'Occidente')])
    valor = models.IntegerField()
    punto_inicial = models.CharField(max_length=100)
    punto_final = models.CharField(max_length=100)
    conductor = models.ForeignKey(conductor, on_delete=models.CASCADE)
    pasajero = models.ForeignKey(pasajero, on_delete=models.CASCADE)
    fecha_arrendamiento = models.DateTimeField()
    estado = models.CharField(max_length=10, choices=[('pendiente', 'Pendiente'), ('asignado', 'Asignado'), ('en curso', 'En curso'), ('finalizado', 'Finalizado'), ('cancelado', 'Cancelado'), ('anulado', 'Anulado')])

    def __str__(self):
        return f"{self.zona} - {self.fecha}"
