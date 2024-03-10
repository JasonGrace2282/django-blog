from django.db import models


class Post(models.Model):
    title = models.TextField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
