from django.db import models


class BlogConfig(models.Model):
    ion_username = models.TextField()

    def __str__(self) -> str:
        return str(self.ion_username)
