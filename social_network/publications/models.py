from django.db import models


class Post(models.Model):
    owner = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE, related_name="posted_publication")
    text = models.TextField()
    pub_date_time = models.DateTimeField(auto_now=True)
    likers = models.ManyToManyField("accounts.Profile", related_name="liked_publication")


class Comment(models.Model):
    post = models.ForeignKey("publications.Post", on_delete=models.CASCADE, related_name="post_comments")
    owner = models.ForeignKey("accounts.Profile", models.CASCADE, related_name="posted_comment")
    text = models.TextField()
    pub_date_time = models.DateTimeField(auto_now=True)
    likers = models.ManyToManyField("accounts.Profile", related_name="liked_comment")
