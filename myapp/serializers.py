from rest_framework import serializers
from myapp.models import Users


class UsersSerializer(serializers.ModelSerializer):
		class Meta:
			model = Users
			fields = ['name']

	
	# def create(self, validated_data):
	# 	return Users.objects.create(**validated_data)

	# def update(self, instance, validated_data):
	# 	instance.name = validated_data.get('name', instance.name)
	# 	instance.save()
	# 	return instance


