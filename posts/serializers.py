from rest_framework import serializers
from .models import Post
from saved_posts.models import SavedPost

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    saved_post_id = serializers.SerializerMethodField()
    saved_post_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    

    def get_saved_post_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            saved_post = SavedPost.objects.filter(
                owner=user, post=obj
            ).first()
            return saved_post.id if saved_post else None
        return None

    class Meta:
        model = Post
        fields = '__all__'
    

