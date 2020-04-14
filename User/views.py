
from django.shortcuts import render, redirect 
from django.contrib import messages 
from django.contrib.auth import login 
from User.backends.AuthenticationBackend import AuthenticationBackend
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 
from django.core.mail import send_mail 
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import get_template 
from django.template import Context 
from User.user_forms.StudentForm import StudentForm
from User.user_forms.StudentLoginForm import StudentLoginForm
from django.db.utils import IntegrityError
from User.user_models.Student import Student
from User.user_models.Kelas import Kelas
from User.user_models.Jurusan import Jurusan
#################### index#######################################  
def index(request): 
    return render(request, 'index.html', {'title':'index'}) 
   
########### register here #####################################  
def register(request): 

    if request.method == 'POST': 
        form = StudentForm(request.POST)#UserRegisterForm(request.POST) 
        
        if form.is_valid():             
            try:
                kelas = Kelas.objects.all().filter(tingkat=int(form.cleaned_data["kelas"]))[0]
                jurusan = Jurusan.objects.all().filter(nama_jurusan=form.cleaned_data["jurusan"])[0]
                name = form.cleaned_data["name"]
                password = form.cleaned_data["password"]
                email = form.cleaned_data["email"]

                student = Student(name=name, password=password, email=email, kelas=kelas, jurusan=jurusan)
                student.save()

                return login_form(request)
            except (IntegrityError):
                #email already exist
                print("email already exist")
                pass
            
            
        else:
            print('form not valid')
            # username = form.cleaned_data.get('username') 
            # email = form.cleaned_data.get('email') 
            ######################### mail system ####################################  
            # htmly = get_template('user / Email.html') 
            # d = { 'username': username } 
            # subject, from_email, to = 'welcome', 'your_email@gmail.com', email 
            # html_content = htmly.render(d) 
            # msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
            # msg.attach_alternative(html_content, "text / html") 
            # msg.send() 
            #messages.success(request, f'Your account has been created ! You are now able to log in') 
            ##################################################################  
            
                
    return render(request, 'register1.html', )#{'form': form, 'title':'reqister here'}) 
    
   
################ login forms###################################################  

def login_form(request): 
    if request.method == 'POST': 
        # AuthenticationForm_can_also_be_used__ 
        print(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        user = AuthenticationBackend().authenticate(request=request, email = email, password = password) 
        if user is not None: 
            form = login(request, user, backend='User.backends.AuthenticationBackend.AuthenticationBackend') 
            messages.success(request, f' wecome {email} !!') 
            return redirect('judger:problem_list') 
        else: 
            messages.info(request, f'account done not exit plz sign in') 
    form = StudentLoginForm() 
    return render(request, 'login.html', {'form':form, 'title':'log in'}) 
