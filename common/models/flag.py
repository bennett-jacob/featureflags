from django.db import models

from ._base import BaseModel


class Flag(BaseModel):
    name = models.SlugField(unique=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
