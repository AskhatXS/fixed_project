from django import forms
from django.shortcuts import redirect

from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']\

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

