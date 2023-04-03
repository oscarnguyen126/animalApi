from rest_framework import serializers
from core.models import Cat


class CatSerializer(serializers.Serializer):
    breed = serializers.CharField()
    age = serializers.CharField()
    size = serializers.CharField()
    gender = serializers.CharField()
    account_id = serializers.IntegerField()

    def create(self):
        return Cat(**self.validated_data)
    
    def update(self, instance, validated_data):
        instance.breed = validated_data.get('breed', instance.breed)
        instance.age = validated_data.get('age', instance.age)
        instance.size = validated_data.get('size', instance.size)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance


class ShowCatSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    breed = serializers.CharField()
    age = serializers.CharField()
    size = serializers.CharField()
    gender = serializers.CharField()
    account_id = serializers.IntegerField()
