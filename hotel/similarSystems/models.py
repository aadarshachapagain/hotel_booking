from django.db import models
from datetime import datetime


class SimilarSystems(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Meta:
    verbose_name_plural = "SimilarSystems"
