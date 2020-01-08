from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image_url', 'is_featured') # i
