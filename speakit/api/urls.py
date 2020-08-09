from .views import *
from django.urls import path
from knox import views as knox_views
from rest_framework import routers

app_name = "api"

router = routers.SimpleRouter()
router.register("posts", PostViewSet)
router.register("get_users_info", GetUsersInfoApi)

urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register"),
    path("login/", LoginApi.as_view(), name="login"),
    path("logout/", knox_views.LoginView.as_view(), name="logout"),
    path("prueba/", Prueba.as_view(), name="prueba"),
    path("validate_username/", ValidateUsernameApi.as_view(), name="validate_username"),
    path("validate_email/", ValidateEmailApi.as_view(), name="validate_email"),
    path("get_user_id/", GetUserIdApi.as_view(), name="get_user_id"),
    path("posts_by_user/", PostByUser.as_view(), name="get_posts_by_user"),
    path("search_users/", SearchUsers.as_view(), name="search_users"),
    #path("get_users_info/", GetUsersInfoApi.as_view(), name="get_users_info")
]

urlpatterns += router.urls