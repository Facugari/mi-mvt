from unittest.util import _MAX_LENGTH
from django.db import models


class Familiares(models.Model):

    nombre = models.CharField(max_length = 30)
    edad = models.IntegerField()
    fecha = models.DateField()