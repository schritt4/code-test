from django.db import models
from django.contrib.auth.models import User

class Club(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    introduction = models.TextField(max_length=100)
    logo = models.ImageField(upload_to='Club', null=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model):
    club = models.ForeignKey(Club, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
