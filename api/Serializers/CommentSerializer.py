from rest_framework import serializers

from falow_app.models import Comment

class CommentSerializer(serializers.ModelSerializer):

  class Meta:
    model = Comment
    fields = "__all__"