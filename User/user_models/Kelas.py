from django.db import models
from .Jurusan import Jurusan
class Kelas(models.Model):
    tingkat = models.IntegerField(unique=True)