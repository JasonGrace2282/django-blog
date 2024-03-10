from django.db import models


class Post(models.Model):
    title = models.TextField(default="hi")
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
