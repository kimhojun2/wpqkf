from django.urls import path, include
from . import views

urlpatterns = [
    path('resign/', views.resign),
    path('test/', views.test)
]