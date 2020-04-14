from django.urls import path
from . import views
app_name = 'get_student'

urlpatterns = [
  path('all/', views.index, name='student_list'),
  path('presensi/', views.presensi, name='presensi'),
  
]
