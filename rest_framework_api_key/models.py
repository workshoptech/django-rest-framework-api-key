import uuid

from django.db import models


class APIKeyManager(models.Manager):

    def is_valid(self, api_key):
        return self.filter(key=api_key).exists()


class APIKey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=50, unique=True)
    key = models.CharField(max_length=40, unique=True)

    objects = APIKeyManager()

    class Meta:
        verbose_name_plural = "API Keys"
        ordering = ["-created"]

    def __str__(self):
        return self.name
