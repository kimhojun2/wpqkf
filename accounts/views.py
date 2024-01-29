from django.shortcuts import render
from .models import User
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import CustomRegisterSerializer
from django.utils import timezone
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


def test(request):
    print('연결은 성공!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    return print('리턴도 성공!!!!!!!!!!!!!!!!!!!!!!')