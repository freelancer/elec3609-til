from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10)
    signup_date = models.DateTimeField(auto_now_add=True)
    password_hash = models.CharField(max_length=256)

class Post(models.Model):
    # We will use the implicit ID field
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
