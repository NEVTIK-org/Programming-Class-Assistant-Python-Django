from django.db import models
from User.user_models.Student import Student 
class Presensi(models.Model):
    nama = models.CharField(max_length=50, blank=False)
    kelas = models.CharField(max_length=50, blank=False)
    jurusan = models.CharField(max_length=50, blank=False)
    waktu = models.DateTimeField()
    index = models.IntegerField(default=1)
    student_info = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
        