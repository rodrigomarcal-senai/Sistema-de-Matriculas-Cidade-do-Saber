from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
