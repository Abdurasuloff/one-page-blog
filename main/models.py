from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField()
    image = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
      return self.title