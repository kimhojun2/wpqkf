from django.shortcuts import render
from balls.models import route
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from balls.serializers import LocationSerializer, RouteSerializer, HistorySerializer
from django.http import JsonResponse 
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly


@api_view(['GET'])
def device_history_routes(request, device_seq):
    print(1111111111111111111111)
    histry_data = route.objects.filter().order_by('-created_at')[:5]
    print(histry_data)
    serializer = HistorySerializer(histry_data, many=True)
    print(55555555555555)
    return Response(serializer.data)