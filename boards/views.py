from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Board, Comment
from .serializers import BoardListSerializer, BoardSerializer
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def boardlist(request):
    if request.method == 'GET':
        boards = Board.objects.filter(is_deleted=False)
        serializer = BoardListSerializer(boards, many=True)
        print(request.user)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        print('[POST]요청은 들어옴')
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_seq=request.user)
            print(request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def board_detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'GET':
        print(board.user_seq)
        serializer = BoardSerializer(board)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        if request.user.id == board.user_seq_id:
            serializer = BoardSerializer(board, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                print('형식 고쳐와')
        else:
            print('[PUT]너가 쓴글 아니야')
    
    elif request.method == 'DELETE':
        if request.user.id == board.user_seq_id:
            board.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            print('[DELETE]너가 쓴글 아니야')
    

