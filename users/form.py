from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser
class RegisterForm(UserCreationForm):

    class Meta:
        model=CustomUser
        fields=['username','email','password1','password2','role']


from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']