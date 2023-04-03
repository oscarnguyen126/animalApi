from rest_framework import serializers
from core.models import Dog


class DogSerializer(serializers.Serializer):
    breed = serializers.CharField()
    origin = serializers.CharField()
    color = serializers.CharField()
    height = serializers.CharField()
    eyes_color = serializers.CharField()
    longevity = serializers.CharField()
    character = serializers.CharField()
    health_problems = serializers.CharField()
    account_id = serializers.IntegerField()

    def create(self):
        return Dog(**self.validated_data)
    
    def update(self, instance, validated_data):
        instance.breed = validated_data.get('breed', instance.breed)
        instance.origin = validated_data.get('origin', instance.origin)
        instance.color = validated_data.get('color', instance.color)
        instance.height = validated_data.get('height', instance.height)
        instance.eyes_color = validated_data.get('eyes_color', instance.eyes_color)
        instance.longevity = validated_data.get('longevity', instance.longevity)
        instance.character = validated_data.get('character', instance.character)
        instance.health_problems = validated_data.get('health_problems', instance.health_problems)
        instance.save()
        return instance


class ShowDogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    breed = serializers.CharField()
    origin = serializers.CharField()
    color = serializers.CharField()
    height = serializers.CharField()
    eyes_color = serializers.CharField()
    longevity = serializers.CharField()
    character = serializers.CharField()
    health_problems = serializers.CharField()
    account_id = serializers.IntegerField()