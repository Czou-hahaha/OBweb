from django.db import models
from universities.models import University


class Program(models.Model):
    DEGREE_CHOICES = [
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('phd', 'PhD'),
    ]

    FIELD_CHOICES = [
        ('engineering', 'Engineering'),
        ('business', 'Business'),
        ('social_sciences', 'Social Sciences'),
        ('arts', 'Arts'),
        ('medicine', 'Medicine'),
        ('science', 'Science'),
    ]

    name = models.CharField(max_length=200)
    chinese_name = models.CharField(max_length=200)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='programs')
    degree_type = models.CharField(max_length=20, choices=DEGREE_CHOICES)
    field = models.CharField(max_length=20, choices=FIELD_CHOICES)
    duration = models.CharField(max_length=50)
    description = models.TextField()
    requirements = models.TextField()
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    application_deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['university', 'name']

    def __str__(self):
        return f"{self.name} - {self.university.name}"
