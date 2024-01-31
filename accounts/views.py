from django.shortcuts import render
from .models import User
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import CustomRegisterSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import permission_classes
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
# Create your views here.

def resign(request):
    user = get_object_or_404(User, username=request.user)
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    token = Token.objects.get(user=request.user)
    print('%%%%%%%%%%%%%%%%%%%%%%%%%', token)
    user.is_active = False
    user.resigned_at = timezone.now()
    user.save()
    print(user.is_resigned)
    return render(request)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile(request, username):
    if request.method == 'GET':
        user_profile = get_object_or_404(User, username=username)
        serializer = CustomRegisterSerializer(user_profile)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        user_profile = get_object_or_404(User, username=username)
        serializer = ProfileSerializer(user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)



def test(request):
    print('연결은 성공!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    return print('리턴도 성공!!!!!!!!!!!!!!!!!!!!!!')