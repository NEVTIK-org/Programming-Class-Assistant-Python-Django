from django.db import models

class Jurusan(models.Model):
    nama_jurusan = models.CharField(max_length=25, unique=True)
