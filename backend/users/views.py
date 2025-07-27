from rest_framework.generics import CreateAPIView

from .serializers import RegisterSerializer

from django.shortcuts import render


def frontend_login(request):
    return render(request, "login.html")


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
