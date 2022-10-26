from rest_framework import serializers

from Accounts.models import UserRegistation

class UserRegistationSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = UserRegistation
        fields = ('id', 'full_name', 'email', 'pNumber', 'password')

    def create(self, validated_data):
        return UserRegistation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.email = validated_data.get('email', instance.email)
        instance.pNumber = validated_data.get('pNumber', instance.pNumber)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance