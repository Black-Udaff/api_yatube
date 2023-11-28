from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        

        fields = ('id', 'text', 'author', 'group', 'image', 'pub_date')
        read_only_fields = ('author',)
