from django.urls import path
from .views import ListAsView, DetailAsView

urlpatterns = [
    path('<int:pk>', DetailAsView.as_view()),
    path('', ListAsView.as_view()),
    ]
