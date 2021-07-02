from django.db import models


class Link(models.Model):
    link = models.URLField(unique=True)

    def __str__(self):
        return self.link
