from rest_framework import serializers
from apps.news.models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'publication_time']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fileds = ['id', 'title', 'picture', 'publication_time', 'content', 'authoe', 'comments']