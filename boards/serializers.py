from rest_framework import serializers
from .models import Board, Comment
from accounts.models import User


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username')


class BoardListSerializer(serializers.ModelSerializer):
    # user_seq = UserSerializer()
    class Meta:
        model = Board
        fields = ('user_seq', 'title', 'content', 'created_at','id',)


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ('user_seq',)
