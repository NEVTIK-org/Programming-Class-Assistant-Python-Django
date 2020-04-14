from django import forms  
from GetStudent.getstudent_models.Presensi import Presensi

class PresensiForm(forms.Form):  
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
        