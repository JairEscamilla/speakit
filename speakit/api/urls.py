from .views import *
from django.urls import path
from knox import views as knox_views

app_name = "api"

urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register"),
    path("login/", LoginApi.as_view(), name="login"),
    path("logout/", knox_views.LoginView.as_view(), name="logout"),
    path("prueba/", Prueba.as_view(), name="prueba"),
    path("validate_username/", ValidateUsernameApi.as_view(), name="validate_username"),
    path("validate_email/", ValidateEmailApi.as_view(), name="validate_email")
]