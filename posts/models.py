from django.db import models


class Post(models.Model):
    title = models.TextField(default="hi")
    body = models.TextField()

    def __str__(self):
        return str(self.title)
