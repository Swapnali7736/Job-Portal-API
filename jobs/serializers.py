from rest_framework import serializers
from jobs.models import Job
from django.contrib.auth.models import User

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields='__all__'
        read_only_fields=['postedby']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password',"first_name","last_name"]


    def create(self,validated_data):
        return User.objects.create_user(**validated_data)        