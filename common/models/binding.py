from django.db import models

from ._base import BaseModel
from .flag import Flag


class Binding(BaseModel):
    flag: Flag = models.ForeignKey(
        Flag, on_delete=models.CASCADE, related_name="bindings"
    )
    subject = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.flag} <> {self.subject}"

    class Meta:
        unique_together = (("flag", "subject",),)
