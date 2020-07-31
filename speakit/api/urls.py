from .views import *
from django.urls import path
from knox import views as knox_views

app_name = "api"

urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register"),
    path("login/", LoginApi.as_view(), name="login"),
    path("logout/", knox_views.LoginView.as_view(), name="logout"),
    path("prueba/", Prueba.as_view(), name="prueba")
]