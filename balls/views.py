from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import location, route
from accounts.models import User
from .serializers import LocationSerializer, RouteSerializer, HistorySerializer
from django.http import JsonResponse 
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def quizball(request, quiz_num):
    quiz_data = get_list_or_404(location, is_quiz=1)
    quiz = quiz_data[quiz_num]
    serializer = LocationSerializer(quiz)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def quiz_answer(request, quiz_num):
    quiz_data = get_list_or_404(location, is_quiz=1)

    if 0 <= quiz_num < len(quiz_data):
        target = quiz_data[quiz_num]
        print(target.id)
        quiz_answer_data = get_list_or_404(route, loca_seq=target)[0]
        print(quiz_answer_data)
        serializer = RouteSerializer(quiz_answer_data)
        return Response(serializer.data)
    
    else:
        return Response({'message': 'No Quiz'}, status=404)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def my_history_route(request, username):
    user = get_object_or_404(User, username=username)
    user_id = user.pk
    # histry_data = get_list_or_404(route, user_seq=user_id)
    histry_data = route.objects.filter(user_seq=user_id).order_by('-created_at')[:10]
    serializer = HistorySerializer(histry_data, many=True)
    return Response(serializer.data)