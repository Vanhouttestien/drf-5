from django.db.models import Count
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
    queryset = Post.objects.annotate(
        saved_post_count=Count('save_post', distinct=True)).order_by('-created_at')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['language', 'age', 'level', 'saved_post_count']
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    retrieve post 
    owner can edit or delete post 
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        saved_post_count=Count('save_post', distinct=True)
    ).order_by('-created_at')

