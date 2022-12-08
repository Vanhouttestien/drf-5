from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(generics.ListCreateAPIView):
    """
    list all profiles
S
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


    
class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    get a profile
    owner can update

    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
