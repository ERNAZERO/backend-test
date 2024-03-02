from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from user.models import User
from .models import Post, Comment, Like


class PostSerializer(serializers.ModelSerializer):

    author = serializers.CharField(
        read_only=True
    )
    created_at = serializers.CharField(
        read_only=True
    )

    class Meta:
        model = Post
        fields = "__all__"

        def get_image_url(self, obj):
            request = self.context.get('request')
            image_url = obj.fingerprint.url
            return request.build_absolute_url(image_url)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ["text"]


class LikeSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Like
        fields = ['author', 'post']