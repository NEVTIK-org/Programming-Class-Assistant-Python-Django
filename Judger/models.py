from django.db import models
from User.models import Student
# from Judger.judger_models.problem import Problem
# Create your models here.

#Student, Problem, Score
class StuProSco(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
    problem = models.CharField(max_length=100)
    score = models.IntegerField()

