from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.http import HttpResponse
from random import choice
from GetStudent.forms.PresensiForm import PresensiForm
from GetStudent.getstudent_models.Presensi import Presensi
import socket    
from User.user_models.Student import Student
from django.contrib import messages 
import datetime
# Create your views here.


def index(request):
    if (request.method=="GET"):
        presentions = list(Presensi.objects.all())
        hostname = socket.gethostname()    
        IPAddr = socket.gethostbyname(hostname)    
        return render(request, "student_list.html", {"presentions": presentions, "ip": IPAddr})        
        #return HttpResponse(str(len(students)), content_type="text")

student_index = 1
def presensi(request):
    global student_index
    if (request.method=="POST"):
        form = PresensiForm(request.POST)
        if (form.is_valid()):
            student = Student.objects.filter(email=form.cleaned_data["email"], password=form.cleaned_data["password"])
            if (len(student)==0):
                messages.error(request, "Wrong Username or Password")
            else:
                student = student[0]
                db = Presensi(
                    nama=student.name,
                    kelas=str(student.kelas.tingkat),
                    jurusan=student.jurusan.nama_jurusan,
                    waktu=datetime.datetime.now(),
                    index=student_index,
                    student_info=student
                    )
                student_index+=1
                db.save()
                return redirect('get_student:student_list')
    return render(request, f"presensi_login.html")

# def register(request):
#     max_student = 16
#     form = StudentForm(request.POST or None)
#     if (request.method=="POST"):
#         if (form.is_valid()):
#             #get the all index
#             students_index = set([i.index for i in Student.objects.all()])
#             all_pos = list(set([i for i in range(1, max_student+1)]) - students_index)

#             if (not (len(all_pos)<=0)):
#                 new_index = choice(all_pos)
#                 name = form.cleaned_data["name"]
#                 kelas  = form.cleaned_data["kelas"]
#                 username  = form.cleaned_data["username"]
#                 password  = form.cleaned_data["password"]
#                 new_student = Student(name=name, kelas=kelas, index=new_index, username=username, password=password)
#                 new_student.save()
#             return redirect("get_student:student_list")
#     return render(request, "student_form.html", {'form':form})
        

# class StudentCreate(CreateView):
#     model = Student
#     fields = ['name', 'kelas']
#     success_url = reverse_lazy('get_student:student_list')
#     max_student = 16

#     def form_valid(self, form):
#         nama = form.cleaned_data['name']
#         kelas = form.cleaned_data['kelas']
        
#         #get the all index
#         students_index = set([i.index for i in Student.objects.all()])
#         all_pos = list(set([i for i in range(1, self.max_student+1)]) - students_index)
#         new_index = choice(all_pos)
#         new_student = Student(name=nama, kelas=kelas, index=new_index)
#         new_student.save()

#         return redirect(self.request, "all")


#     def get_context_data(self, **kwargs):
#         context = super(StudentCreate, self).get_context_data(**kwargs)
#         context = super().get_context_data(**kwargs)
#         context["max_student"] = str(list(range(100)))
#         return context

        





    