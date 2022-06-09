from django_unicorn.components import UnicornView
from django import forms
from django.shortcuts import redirect
from core.models import Usuario


class SignupForm(forms.Form):
    username=forms.CharField(max_length=255, required=True)
    password=forms.CharField(max_length=255, required=True)
    name =forms.CharField(max_length=255, required=True)


class SignupView(UnicornView):
    username=""
    password=""
    name = ""

    error = ""

    def signup(self):
        if self.is_valid():
            user = Usuario.objects.create(username=self.username, name=self.name)
            user.set_password(self.password)
            try:
                user.save()
                return redirect('index')
            except:
                self.error= "Algo deu errado, tente novamente!"

