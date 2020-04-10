from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Book(models.Model):
    title = models.TextField(null=False, blank=False)
    amazon_url = models.URLField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    genre = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
