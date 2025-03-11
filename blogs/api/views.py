from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.exceptions import ValidationError,NotFound
from .serializers import *
from blogs.models import Post, Comments




class ListCreatePostView(generics.ListCreateAPIView):
     
     queryset = Post.objects.all()
     serializer_class = AddPostSerializer
     permission_classes = [IsAuthenticated]


     def get_queryset(self):
         
         return Post.objects.filter(author = self.request.user)
     


     def perform_create(self, serializer):
          
          return serializer.save(author = self.request.user)


class ListPostView(generics.ListAPIView):
     
     queryset = Post.objects.all()
     serializer_class = PostListSerializer
     permission_classes = [AllowAny]

     def get_queryset(self):
         
         return Post.objects.filter(status = 'published')


class DetailPostView(generics.RetrieveDestroyAPIView):
     
     queryset = Post.objects.all()
     serializer_class = PostDetailSerializer
     permission_classes = [IsAuthenticated]


     def get_queryset(self):
        return Post.objects.filter(id =self.kwargs['pk'])
     

     def perform_update(self, serializer):
        
        serializer.save(user = self.request.user)



     def perform_destroy(self, instance):
        
        instance.delete() 
    

class CommentListCreateView(generics.ListCreateAPIView):

    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):

        post_id = self.kwargs['pk']

        try:
           post =  Post.objects.get(id = post_id)
        
        except Post.DoesNotExist:
            return ValidationError({"detail":"No post available"}, status=status.HTTP_404_NOT_FOUND)
        
        
        return serializer.save(post = post)
    
    def get_queryset(self):
        
        post_id = self.kwargs['pk']

        if post_id:
            comments =  Comments.objects.filter(post_id=post_id)
        
        if not comments.exists():
            raise NotFound(detail="No comments available for this post.", code=status.HTTP_404_NOT_FOUND)
        
        return comments
        


        
        

        























'''class BlogPostView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self,request):

        data = request.data
        serializer = AddPostSerializer(data=data, context = {'request':request})
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):

        data = request.data
        
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)
        

        serializer = AddPostSerializer(post,data =data, partial = True, context={'request':request})
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

    
class BlogListView(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]


class BlogPostDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        try:
            post = Post.objects.get(id=pk)  
        except Post.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PostDetailSerializer(post)  
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,pk):

        try:
             post = Post.objects.get(id = pk)

        except Post.DoesNotExist:
            return Response({'Post not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        post.delete()

        return Response({'Post deleted.'},status=status.HTTP_200_OK)'''
    
