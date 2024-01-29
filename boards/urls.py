from django.urls import path, include
from . import views

urlpatterns = [
    path('boardlist/', views.boardlist),
    path('boardlist/<int:board_pk>/', views.board_detail),
]