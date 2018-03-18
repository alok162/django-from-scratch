from rest_framework import serializers
from myapp.models import Users


class UsersSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=200)

	def create(self, validated_data):
		return Users.objects.create(**validated_data)
	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.save()
		return instance

  #   def update(self, instance, validated_data):
  #       instance.name = validated_data.get('name', instance.name)
  #      	instance.save()
  #       return instance
