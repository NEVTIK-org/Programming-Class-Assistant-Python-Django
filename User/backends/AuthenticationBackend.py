from django.conf import settings
from django.contrib.auth.hashers import check_password
from User.user_models.Student import Student


class AuthenticationBackend:
    def authenticate(self, request, email=None, password=None):
        student = Student.objects.filter(email=email, password=password)
        if len(student)==0:
            return None
        else:
            return student[0]

    def get_user(self, user_id):
        try:
            return Student.objects.get(pk=user_id)
        except Student.DoesNotExist:
            return None