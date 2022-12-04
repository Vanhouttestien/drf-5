from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import SavedPost
from .serializers import SavedPostSerializer
from django_filters.rest_framework import DjangoFilterBackend

class SavedPostList(generics.ListCreateAPIView):
    """
    List all saved posts
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SavedPostSerializer
    queryset = SavedPost.objects.all()

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class SavePostDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SavedPostSerializer
    queryset = SavedPost.objects.all()
