from django.urls import path
from .views import (PostListView,
                    CreatePostView,
                    DeletePostView,
                    AddCommentView,
                    PostDetailView,
                    LikeView)
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('post_list/', PostListView.as_view(), name='see_post'),
    path('<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('post_create/', CreatePostView.as_view(), name='create_post'),
    path('post_delete/<int:id>', DeletePostView.as_view(), name='delete-post'),
    path('<int:post_id>/comments/', AddCommentView.as_view(), name='add-comment'),
    path('<int:post_id>/like', LikeView.as_view(), name='liking')
]