import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import localtime


# Create your models here.
# class PublishedObj(models.Model):
#     author = models.ForeignKey(User, related_name="published_obj", on_delete=models.CASCADE)
#     pub_date = models.DateTimeField(auto_now=True)
#     like_users = models.ForeignKey(User, related_name="published_obj", blank=True, on_delete=models.CASCADE)

class Post(models.Model):
    author = models.ForeignKey(User, related_name='user_posts', on_delete=models.CASCADE)
    text = models.TextField(max_length=2048)
    pub_date = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(User, related_name="liked_posts", blank=True)

    def __str__(self):
        return f"{self.author} publication at {localtime(self.pub_date).strftime('%d-%m-%Y %H:%M')}"

    def __repr__(self):
        values = (value for value in self.__dict__.values())
        return f"Publication{values}"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    text = models.TextField(max_length=512)
    pub_date = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(User, related_name="liked_comments", blank=True)

    def __str__(self):
        return f"{self.author} comment at {localtime(self.pub_date).strftime('%d-%m-%Y %H:%M')}"

    def __repr__(self):
        values = (value for value in self.__dict__.values())
        return f"Comment{values}"
