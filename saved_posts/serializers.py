from rest_framework import serializers
from .models import SavedPost


class SavedPostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
  
    class Meta:
        model = SavedPost
        fields = '__all__'
    

