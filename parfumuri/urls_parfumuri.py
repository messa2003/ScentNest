from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),  # Adaugă un prefix clar
]
