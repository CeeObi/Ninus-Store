from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control form-group my-0 rounded-0",
                "data-toggle": "username",
                "id": "username",
                "name": "username"
            }
        ),
    )
    password = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control form-group my-0 rounded-0",
                "data-toggle": "password",
                "id": "password",
                "name": "password",
            }
        ),
    )
    class Meta:
        model = User
        fields = ["username", "password"]


class SignUpForm(AuthenticationForm):
    firstname = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Firstname",
                "class": "form-control form-group my-0 rounded-0",
                "data-toggle": "firstname",
                "id": "firstname",
                "name": "firstname"
            }
        ),
    )
    lastname = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Lastname",
                "class": "form-control form-group my-0 rounded-0",
                "data-toggle": "lastname",
                "id": "lastname",
                "name": "lastname"
            }
        ),
    )
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control form-group my-0 rounded-0",
                "data-toggle": "username",
                "id": "username",
                "name": "username"
            }
        ),
    )
    email = forms.EmailField(
        max_length=50,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control form-group my-0 rounded-0",
                "data-toggle": "email",
                "id": "email",
                "name": "email"
            }
        ),
    )

    password = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control form-group my-0 rounded-0",
                "data-toggle": "password",
                "id": "password",
                "name": "password",
                "minlength": "3"
            }
        ),
    )
    class Meta:
        model = User
        fields_order = ["firstname","lastname","username","email","password"]