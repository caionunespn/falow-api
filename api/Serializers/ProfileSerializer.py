from rest_framework import serializers, status
from rest_framework.response import Response

from falow_app.models import Profile
# from curae_app.utils import createProfileImage64

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db.models.base import ObjectDoesNotExist
from django.contrib.auth.password_validation import validate_password

class ProfileSerializer(serializers.ModelSerializer):

  def create(self, request):
    context = self.context['request'].data
    try:
      check_user = User.objects.get(username=context['email'])
      raise serializers.ValidationError('User already exists')

    except ObjectDoesNotExist:
      password = validate_password(context['password'])

      try:
        new_user = User(email=context['email'], username=context['email'])
        new_user.set_password(context['password'])

        new_profile = super(ProfileSerializer, self).create(request)
        new_profile.user = new_user

        new_user.save()
        new_profile.save()
        return new_profile

      except Exception as e:
        raise serializers.ValidationError(str(e))
    
    except Exception as e:
      raise serializers.ValidationError(str(e))

  class Meta:
    model = Profile
    fields = "__all__"