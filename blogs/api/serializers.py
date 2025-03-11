from rest_framework import serializers
from blogs.models import Post,PostImage,Comments




class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title','description','images','status','created_at']

class PostDetailSerializer(serializers.ModelSerializer):

    images = PostImageSerializer(many=True, read_only=True) 

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['updated_at']
    
class AddPostSerializer(serializers.ModelSerializer):

    images = serializers.ListField(
        child=serializers.ImageField(), 
        required=False  
    )


    class Meta:
        fields = ['title','description','images','status']


    
    def create(self, validated_data):
        images = validated_data.pop('images', [])
        post = Post.objects.create(**validated_data)

        for image in images:
            PostImage.objects.create(post=post, image=image)
        
        return post
    

    
    def update(self, instance, validated_data):
        
        images = validated_data.pop('images', None)  

        
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        
        if images is not None:
            
            instance.images.all().delete()

            for image in images:
                PostImage.objects.create(post=instance, image=image)

        return instance
    




class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ['post','content','author','created_at']
        read_only_fields = ['post','author','created_at']