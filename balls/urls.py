from django.urls import path
from . import views

urlpatterns = [
    path('quiz/<int:quiz_num>/', views.quizball),
    path('quiz_ans/<int:quiz_num>/', views.quiz_answer),
    # path('myhistory/<str:username>/', views.my_history_route),
]