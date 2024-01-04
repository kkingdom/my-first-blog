from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    photo = models.ImageField(upload_to='static/profile_pics')
    create_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
