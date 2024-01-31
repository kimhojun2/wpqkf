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


class CommentSerializer(serializers.ModelSerializer):
    class BoardSeqSerializer(serializers.ModelSerializer):
        class Meta:
            model = Board
            fields = ('board_seq',)
    
    Board_seq = BoardSeqSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
