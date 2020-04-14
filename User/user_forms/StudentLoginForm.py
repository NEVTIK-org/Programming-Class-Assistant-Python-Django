from django import forms  

class StudentLoginForm(forms.Form):  
    email = forms.CharField(max_length=30, required=True)
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput())