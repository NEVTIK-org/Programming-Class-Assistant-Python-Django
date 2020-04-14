
#from ProgrammingClass.universal_models.Student import Student
from User.user_models.Student import Student
from django import forms  
class StudentForm(forms.Form):  
    email = forms.CharField(max_length=30, required=True)
    password = forms.CharField(max_length=30, required=True)
    name = forms.CharField(max_length=30, required=True)
    kelas = forms.CharField(max_length=10, required=True)
    jurusan = forms.CharField(max_length=10, required=True)
    
    # class Meta:  
    #     model = Student
    #     fields = "__all__"  