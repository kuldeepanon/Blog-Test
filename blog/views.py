from .models import Post, Comment
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, permissions, status
from rest_framework.pagination import PageNumberPagination
from .serializers import PostSerializer, CommentSerializer,UserSerializer
        
# Create your views here.
        
class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PostPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def like_post(self, request, pk=None):
        post = self.get_object()
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            return Response({'status': 'unliked'}, status=status.HTTP_204_NO_CONTENT)
        else:
            post.likes.add(request.user)
            return Response({'status': 'liked'}, status=status.HTTP_200_OK)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id'] 
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, post=post)