from django.urls import path
from .views import CalculateView, HistoryView, frontend_index

urlpatterns = [
    path('calculate/', CalculateView.as_view()),
    path('history/', HistoryView.as_view()),
    path('', frontend_index),
]
