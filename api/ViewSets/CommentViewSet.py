from rest_framework import viewsets

from falow_app.models import Comment

from api.Serializers.CommentSerializer import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
