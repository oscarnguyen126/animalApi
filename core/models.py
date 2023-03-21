from django.db import models


class Todo(models.Model):
    content = models.TextField()
    completed = models.BooleanField(default=False)

    def __repr__(self):
        return f"<Todo: content={self.content}, completed={self.completed}>"
