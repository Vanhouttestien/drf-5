from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend

class PostList(generics.ListCreateAPIView):
    """
    List all posts
    create post if logged in 
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['language', 'age', 'level']
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    retrieve post 
    owner can edit or delete post 
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

