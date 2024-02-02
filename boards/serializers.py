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
        fields = ('id', 'user_seq', 'title', 'content', 'created_at')




# class CommentListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ('id', 'user_seq', 'board_seq', 'created_at', 'updated_at', 'is_deleted')


class CommentSerializer(serializers.ModelSerializer):
    # user_seq = serializers.ReadOnlyField(source = 'user.id')
    # board_seq = serializers.ReadOnlyField(source = 'board.id')
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user_seq', 'board_seq')


class BoardSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, source='comments.all')
    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ('user_seq',)

