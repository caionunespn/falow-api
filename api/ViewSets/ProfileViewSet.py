from rest_framework import viewsets

from falow_app.models import Profile
from falow_app.permissions import IsPostOrIsAuthenticated

from api.Serializers.ProfileSerializer import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
  permission_classes = (IsPostOrIsAuthenticated,)
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer
