from rest_framework import serializers

from falow_app.models import Post
# from curae_app.utils import createProfileImage64

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = "__all__"