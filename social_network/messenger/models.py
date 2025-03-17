from django.db import models


class Message(models.Model):
    chat = models.ForeignKey("messenger.PersonalChat", related_name="messages", on_delete=models.CASCADE)
    text = models.TextField(max_length=2048)
    owner = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE, related_name="messages")
    pub_date_time = models.DateTimeField(auto_now=True)


class PersonalChat(models.Model):
    members = models.ManyToManyField("accounts.Profile")


class Group(PersonalChat):
    pass
    # admins = models.ManyToManyField("accounts.Profile")
