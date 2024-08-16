from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """Class for form for user registration and login"""
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'telephone',
                  'user_type', 'password', 'password2')


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=254)
