from django.contrib import admin
from django.urls import path,include
from website.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("website/user/register/", CreateUserView.as_view(), name="register"),
    path("website/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("website/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("website-auth/", include("rest_framework.urls")),
    path("website/", include("website.urls"))
]
