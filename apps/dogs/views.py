from django.shortcuts import get_object_or_404
from .serializers import DogSerializer, ShowDogSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from core.models import Dog


class DogViewSet(viewsets.ViewSet):
    queryset = Dog.objects.all()

    def list(self, request):
        serializer = ShowDogSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        dog = serializer.create()
        dog.save()
        return Response({"result": serializer.data})

    def retrieve(self, request, pk=None):
        dog = get_object_or_404(self.queryset, pk=pk)
        serializer = ShowDogSerializer(dog)
        return Response(serializer.data)

    def update(self, request, pk=None):
        dog = get_object_or_404(self.queryset, pk=pk)
        serializer = DogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dog.__dict__.update(request.data)
        dog.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        dog = get_object_or_404(self.queryset, pk=pk)
        dog.delete()
        return Response({"msg": "Dog has been removed"})
