from rest_framework import serializers

from falow_app.models import Like

class LikeSerializer(serializers.ModelSerializer):

  class Meta:
    model = Like
    fields = "__all__"