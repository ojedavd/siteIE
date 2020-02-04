from django.db import models

class Pagos(models.Model):
    user_id = models.IntegerField()
    alumno = models.IntegerField()
    curso = models.CharField(max_length=250)
    curso_id = models.IntegerField()
    cuota_id = models.IntegerField()
    fecha = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=20)
    sede_id = models.IntegerField()
    tipo = models.CharField(max_length=20)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    user_created = models.CharField(max_length=20)
    user_modified = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'pagos'
        verbose_name = "pago"
        verbose_name_plural = "pagos"
        ordering = ["-modified"]

    def __str__(self):
        return self.curso