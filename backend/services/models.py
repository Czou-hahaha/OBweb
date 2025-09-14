from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=200)
    chinese_name = models.CharField(max_length=200)
    description = models.TextField()
    chinese_description = models.TextField()
    price = models.CharField(max_length=100)
    features = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
