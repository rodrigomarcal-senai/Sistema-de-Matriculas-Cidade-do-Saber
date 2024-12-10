from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("login_f/", views.login_user, name="login"),
]