from django.db import models


class IonUser(models.Model):
    ion_username = models.TextField()

    def __str__(self) -> str:
        return str(self.ion_username)
