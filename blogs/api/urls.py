from django.urls import path
from .views import ListCreatePostView,ListPostView, DetailPostView,CommentListCreateView


urlpatterns = [

    path('posts/', ListPostView.as_view(), name='post-list'),
    path('my-posts/',ListCreatePostView.as_view(),name='create-post'),
    path('posts/<int:pk>/', DetailPostView.as_view(), name='detail-post'),
    path('comments/<int:pk>/', CommentListCreateView.as_view(), name='comment-list-create'),
]