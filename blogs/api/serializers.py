from rest_framework import serializers
from blogs.models import Post,Comments




'''class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id','image']'''


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id','title','description','image','author','created_at']

class PostDetailSerializer(serializers.ModelSerializer):

    ##images = PostImageSerializer(many=True, read_only=True) 

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at','author','slug']
    
class AddPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title','description','image','status']



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ['post','content','author','created_at']
        read_only_fields = ['post','author','created_at']