from django.db import models


class University(models.Model):
    name = models.CharField(max_length=200)
    chinese_name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    ranking = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    website = models.URLField(max_length=200)
    logo = models.ImageField(upload_to='university_logos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['ranking', 'name']

    def __str__(self):
        return self.name
