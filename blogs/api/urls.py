from django.urls import path
from .views import BlogListView,BlogPostView,BlogPostDetailView


urlpatterns = [
    path('',BlogListView.as_view(), name='blog-list'),
    path('create/', BlogPostView.as_view(), name='create-post'),
    path('update/<int:pk>', BlogPostView.as_view(), name='update-post'),
    path('detail/<int:pk>', BlogPostDetailView.as_view(), name='post-detail'),
    path('delete/<int:pk>', BlogPostDetailView.as_view(), name='post-delete'), 
]