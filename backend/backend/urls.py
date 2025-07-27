from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include
from calculator.views import frontend_index
from users.views import frontend_login  
from django.shortcuts import render

urlpatterns = [
    path('login/', frontend_login, name='login'),
    path('register/', lambda request: render(request, "register.html")),
    path('', frontend_index, name='home'),
    path("admin/", admin.site.urls),
    path("user/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("user/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user/register/", include("users.urls")),
    path("api/calculator/", include("calculator.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
]

