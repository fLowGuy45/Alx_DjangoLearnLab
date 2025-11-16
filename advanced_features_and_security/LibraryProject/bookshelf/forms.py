# LibraryProject/bookshelf/forms.py
from django import forms
from .models import Book, CustomUser

# ExampleForm as required by checker
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # or any model you want to use
        fields = '__all__'

# Optional: Keep the existing CustomUser forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo')
