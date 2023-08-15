from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class UserLoginForm(AuthenticationForm):
  username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 450px;'}))
  password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))


class UserRegisterForm(UserCreationForm):
  username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 430px;'}))
  email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control', 'style': 'width: 350px;'}))
  password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width: 430px;'}))
  password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))

  class Meta:
    model = User 
    fields = ('username', 'email', 'password1', 'password2')


class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review 
    fields = '__all__'