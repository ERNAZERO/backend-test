import os

from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from user.models import User
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .models import Post, Comment, Like
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from user.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class PostPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination


class CreatePostView(APIView):
    permissions = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        user = User.objects.get(id=self.request.user.id)
        if serializer.is_valid():
            post = Post.objects.create(
                image=request.data['image'],
                description=request.data['description'],
                author=user
            )
            post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeletePostView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def delete(self, request, id):
        post = get_object_or_404(Post, id=id)
        if post:
            post.delete()
            return Response({"Post has deleted!"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "ERROR"}, status=status.HTTP_400_BAD_REQUEST)


class AddCommentView(generics.CreateAPIView):
    permissions = [IsAuthenticated]

    def post(self, request, post_id):
        user = User.objects.get(id=request.user.id)
        post = get_object_or_404(Post, id=post_id)
        serializer = CommentSerializer(data=request.data)


        if serializer.is_valid():
            serializer.save(author=user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post_serializer = PostSerializer(post)
        comments = Comment.objects.filter(post=post)
        comment_serializer = CommentSerializer(comments, many=True)
        data = {
            'post': post_serializer.data,
            'comments': comment_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


class LikeView(generics.GenericAPIView):
    permissions = [IsAuthenticated]
    serializer_class = LikeSerializer

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        user = User.objects.get(id=request.user.id)
        like, created = Like.objects.get_or_create(author=user, post=post)
        if not created:
            like.delete()
            return Response({"message": "Like removed."}, status=status.HTTP_200_OK)
        serializer = self.get_serializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)