from rest_framework import viewsets

from falow_app.models import Like

from api.Serializers.LikeSerializer import LikeSerializer

class LikeViewSet(viewsets.ModelViewSet):
  queryset = Like.objects.all()
  serializer_class = LikeSerializer
