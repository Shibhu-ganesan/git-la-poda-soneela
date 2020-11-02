from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, null=False)
    Field = models.CharField(max_length=50, null=False)
    Email = models.EmailField(null=False)
    Query = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.Name
