# LibraryProject/bookshelf/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Book

# Form for creating a new CustomUser
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo')

# Form for updating a CustomUser
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo')

# Example form for Book model
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
