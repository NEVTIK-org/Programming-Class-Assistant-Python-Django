from django.db import models
from .Jurusan import Jurusan
from .Kelas import Kelas
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class Student(AbstractUser):
    email = models.EmailField(_('email'), blank=True, unique=True)
    password = models.CharField(_('password'), max_length=30)
    name = models.CharField(_('nama'), max_length=30, blank=True)
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE, default=1)
    jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE, default=1)
    username=None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'name', 'kelas', 'jurusan']

    