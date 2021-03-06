from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SearchResultStore(models.Model):
    search_key_store = models.CharField(max_length=200)
    date_time_fields = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.search_key_store
    