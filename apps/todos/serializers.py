from rest_framework import serializers
from core.models import Todo


class TodoSerializer(serializers.Serializer):
    content = serializers.CharField()
    completed = serializers.BooleanField(default=False)

    def create(self):
        return Todo(**self.validated_data)
