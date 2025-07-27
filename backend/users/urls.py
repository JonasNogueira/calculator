from django.urls import path
from .views import RegisterView, frontend_login

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('loginn/', frontend_login),
]
