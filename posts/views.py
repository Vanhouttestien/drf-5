from django.db.models import Count
from rest_framework import generics, permissions, filters
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
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = ['age', 'level', 'language', 'save_post__owner__profile']
    ordering_fields = ['created_at', 'saved_post_count']
    search_fields = [
        'owner__username', 
        'title',
        'description',
        ]
    
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

