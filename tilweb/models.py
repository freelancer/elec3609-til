from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    subject = models.CharField(max_length=160)
    content = models.CharField(max_length=800)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    visibility = models.BooleanField(default=False)
    post_date = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    # We will use the implcit id
    tag = models.CharField(max_length=10)
    creation_date = models.DateTimeField(auto_now_add=True)


class PostTag(models.Model):
    post_id = models.ForeignKey(Post)
    tag_id = models.ForeignKey(Tag)
