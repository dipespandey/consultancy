from rest_framework import serializers
from consultapp.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ('url', 'id', 'created', 'title', 'body')
        extra_kwargs = {
            'url': {
                'view_name': 'consultapp:post-detail',
                }
            }

