from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=255, unique=True)


    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

class Discussion(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='discussions')
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='discussions')
    slug = models.SlugField(max_length=255, unique=True)
   
    def __str__(self):
        return self.title

class Answer(models.Model):
    body = models.TextField()
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='answers')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True,null=True) #answer can have many likes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.author.username