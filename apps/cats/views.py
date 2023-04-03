from django.shortcuts import get_object_or_404
from .serializers import CatSerializer, ShowCatSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from core.models import Cat



class CatViewSet(viewsets.ViewSet):
    queryset = Cat.objects.all()

    def list(self, request):
        serializer = ShowCatSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cat = serializer.create()
        cat.save()
        return Response({"result": serializer.data})

    def retrieve(self, request, pk=None):
        cat = get_object_or_404(self.queryset, pk=pk)
        serializer = ShowCatSerializer(cat)
        return Response(serializer.data)

    def update(self, request, pk=None):
        cat = get_object_or_404(self.queryset, pk=pk)
        serializer = CatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cat.__dict__.update(request.data)
        cat.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        cat = get_object_or_404(self.queryset, pk=pk)
        cat.delete()
        return Response({"msg": "Cat has been removed"})
