from rest_framework import viewsets

from falow_app.models import Post

from api.Serializers.PostSerializer import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
