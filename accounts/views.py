from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib.auth.views import LoginView

from .forms import RegisterUserForm, LoginUserForm


class LoginUserView(LoginView):
    form_class = LoginUserForm
    success_url = "dashboard/"


def register_user(request: HttpRequest):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterUserForm()

    context = {"form": form}
    return render(request, "registration/register.html", context)


def login_user(request: HttpRequest):
    if request.method == "POST":
        form = LoginUserForm(request.POST)

        if form.is_valid():
            return form.get_user()
    else:
        form = LoginUserForm()

    context = {"form": form}
    return render(request, "registration/login.html", context)
