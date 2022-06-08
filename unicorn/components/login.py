from django_unicorn.components import UnicornView
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_
from django.contrib.auth import logout as logout_
from django import forms
from core.models import Usuario
from django.shortcuts import redirect


class LoginView(UnicornView):

    has_user = False

    username=""
    password=""

    capa = ""

    name=""

    error = ""


    def check_user(self):
        user = Usuario.objects.filter(username=self.username)
        if user.exists():
            self.error=''
            user = user.first()
            self.capa = str(user.perfil_image.url if user.perfil_image.storage.exists(user.perfil_image.name) else '/static/default-user.jpg')
            self.name = user.name if user.name else user.username
            self.has_user = True

        else:
            self.error = "Invalid username or password"


    def login(self):
        user = authenticate(self.request, username=self.username, password=self.password)
        if user is not None:
            login_(self.request, user)
            return redirect('index')
        else:
            self.error = "Invalid username or password"

