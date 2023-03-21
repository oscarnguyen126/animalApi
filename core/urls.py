from rest_framework.routers import SimpleRouter
from django.contrib import admin
from django.urls import path
from apps.todos.views import TodoViews


todosRouter = SimpleRouter(trailing_slash=False)
todosRouter.register(r"todos", TodoViews, basename="todos")

urlpatterns = [
    path("admin/", admin.site.urls),
] + todosRouter.urls
