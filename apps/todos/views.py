from rest_framework.response import Response
from rest_framework import viewsets
from core.models import Todo
from .serializers import TodoSerializer


class TodoViews(viewsets.ViewSet):
    def list(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response({"result": serializer.data})

    def create(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        todo = serializer.create()
        todo.save()
        return Response({"result": serializer.data})
