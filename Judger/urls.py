from django.urls import path
from django.urls import include
from . import views
app_name = "judger"
urlpatterns = [
    path('test/', include('django.contrib.auth.urls')),
    path('publicscore/', views.public_scoreboard, name="public_scoreboard"),
    path('list/', views.problem_list, name="problem_list"),
    # path('list/<str:problem>/', views.problem_detail, name="problem_detail"),
    path('list/<str:problem>/', views.problem_detail, name="problem_detail"),
    path('upload/answer/<str:problem>/', views.upload_answer, name="upload_answer")
]