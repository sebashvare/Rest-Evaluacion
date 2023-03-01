from django.db import models


"""
Modelo planeacion, contiene los siguientes campos para el formulario en el que interactuan
Los encargados de cada sector para realizar seguimiento.
    
    NUM_ORDEN: Numero de orden la cual se guarda al momento de generar.
    FUENTE: Herramienta que genera la OT.
    CONTRATA: Empresa contratista que le corresponde ejecutar la OT.
    FECHA_PROG: Fecha tentativa en la que se va a ejecutar la OT.
    TIPO_ACTIVIDAD: La actividad que va a ejecutar el contratista segun la OT.
"""


class Planeacion(models.Model):
    orden_trabajo = models.CharField(max_length=20, primary_key=True)
    fuente = models.CharField(max_length=20)
    contrata = models.CharField(max_length=20)
    fecha_programacion = models.DateField()
    estado = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Planeacion'
        verbose_name_plural = 'Modulo Planeacion'

    def __str__(self):
        return str(self.orden_trabajo)


class Hacer(models.Model):
    orden_trabajo = models.ForeignKey(
        Planeacion, related_name="hacers", on_delete=models.CASCADE)
    actividad_ejecutada = models.CharField(max_length=250)
    numero_formato = models.CharField(max_length=20)
    multiplo = models.CharField(max_length=15)
    telemedida = models.CharField(max_length=15)
    actualizac0ion_sistema = models.CharField(max_length=30)
    pagar = models.CharField(max_length=30)
    """
        Un campo que defina el estado de la actividad y enviar al Backlog
    """
    class Meta:
        verbose_name = 'Hacer'
        verbose_name_plural = 'Modulo Hacer'

    def __str__(self):
        return str(self.orden_trabajo) + '-' + str(self.actividad_ejecutada)


class Evaluacion(models.Model):
    orden_trabajo = models.ForeignKey(Planeacion,  on_delete=models.CASCADE)
    primera_factura = models.DateField()
    ultima_telemedida = models.DateField()
    conforme = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Evaluacion'
        verbose_name_plural = 'Modulo Evaluacion'

    def __str__(self):
        return self.orden_trabajo + "-" + self.conforme

    def __unicode__(self):
        return


class Backlog(models.Model):
    """
        Este modelo hace referencia a las alertas que llegan de cualquier fuente que no se una OT.
    """
    fecha = models.DateTimeField(auto_now_add=True)
    fuente = models.CharField(("Quien reporta"), max_length=50)
    reporte = models.CharField(("Que reporta"), max_length=250)
    id_punto_servicio = models.CharField(("ID Punto Servicio"), max_length=15)
    ejecucion = models.CharField(
        ("Quien ejecuta la actividad"), max_length=200)
    estado = models.CharField(("Estado Alerta"), max_length=50)
    responsable = models.CharField(("Quien Resuelve"), max_length=200)
    contrata = models.CharField(("Contratista"), max_length=200)

    class Meta:
        verbose_name = 'Backlog'
        verbose_name_plural = 'Backlogs'

    def __str__(self):
        return "{}-{}".format(str(self.id_punto_servicio), str(self.ejecucion))

    def save(self, *args, **kwargs):
        self.estado = "Pendiente"
        super().save(*args, **kwargs)


class Confiabilidad(models.Model):
    """
        Este modelo hace referencia a Confiabilidad, se tiene como informacion principal
        La OT generada por el modulo de PLaneacion
    """
    CONEXIONADO = [
        ("SEMI", "SEMI"),
        ("DIRECTA", "DIRECTA"),
        ("INDIRECTA", "INDIRECTA"),
        ("GENERACION", "GENERACION")
    ]

    orden_trabajo = models.ForeignKey(Planeacion,  on_delete=models.CASCADE)
    valor_tensiones_a = models.DecimalField(("Valor Tensiones a"), max_digits=5, decimal_places=2)
    valor_tensiones_b = models.DecimalField(("Valor Tensiones b"), max_digits=5, decimal_places=2)
    valor_tensiones_c = models.DecimalField(("Valor Tensiones c"), max_digits=5, decimal_places=2)
    promedio_tensiones = models.DecimalField(("Promedio Tensiones"), max_digits=5, decimal_places=2)
    valor_corrientes_a = models.DecimalField(("Valor Corrientes a"), max_digits=5, decimal_places=2)
    valor_corrientes_b = models.DecimalField(("Valor Corrientes b"), max_digits=5, decimal_places=2)
    valor_corrientes_c = models.DecimalField(("Valor Corrientes c"), max_digits=5, decimal_places=2)
    promedio_corrientes = models.DecimalField(("Promedio Corrientes"), max_digits=5, decimal_places=2)
    angulos_corriente_ia = models.DecimalField(("Angulos Corrientes IA"), max_digits=5, decimal_places=2)
    angulos_corriente_ib = models.DecimalField(("Angulos Corrientes IB"), max_digits=5, decimal_places=2)
    angulos_corriente_ic = models.DecimalField(("Angulos Corrientes IC"), max_digits=5, decimal_places=2)
    sincro_fecha = models.BooleanField(("Sincronizacion Fecha y Hora"))
    validacion_canales = models.BooleanField(("Validacion Canales"))
    cargue_fasorial = models.FileField(("Fasorial"), upload_to="fasorial")
    conexionado = models.CharField(("Conexionado"), max_length=15, choices=CONEXIONADO)
    

    class Meta:
        verbose_name = 'Confiabilidad'
        verbose_name_plural = 'Modulo Confiabilidad'

    def __str__(self):
        return f"{self.orden_trabajo}"
