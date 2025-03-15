from django.db import models


class Post(models.Model):
    owner = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE, related_name="posts")
    text = models.TextField()
    pub_date_time = models.DateTimeField(auto_now=True)
    likers = models.ManyToManyField("accounts.Profile", related_name="liked_posts")


class Comment(models.Model):
    post = models.ForeignKey("publications.Post", on_delete=models.CASCADE, related_name="comments")
    owner = models.ForeignKey("accounts.Profile", models.CASCADE, related_name="comments")
    text = models.TextField()
    pub_date_time = models.DateTimeField(auto_now=True)
    likers = models.ManyToManyField("accounts.Profile", related_name="liked_comments")
