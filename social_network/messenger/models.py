from django.db import models
from django.core.exceptions import ValidationError


class Chat(models.Model):
    member1 = models.ForeignKey("accounts.Profile", on_delete=models.DO_NOTHING, related_name="chats_as_member1")
    member2 = models.ForeignKey("accounts.Profile", on_delete=models.DO_NOTHING, related_name="chats_as_member2")

    def clean(self):
        if self.member1.id == self.member2.id:
            raise ValidationError("You can't create a chat room with yourself")
        if self.member1.id > self.member2.id:
            self.member1, self.member2 = self.member2, self.member1

    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)

    class Meta:
        unique_together = ['member1', 'member2']


class Message(models.Model):
    chat = models.ForeignKey("messenger.Chat", related_name="messages", on_delete=models.CASCADE)
    text = models.TextField(max_length=2048)
    owner = models.ForeignKey("accounts.Profile", related_name="messages", on_delete=models.DO_NOTHING)
    pub_date_time = models.DateTimeField(auto_now=True)


class GroupChat(models.Model):
    title = models.CharField(max_length=32)
    members = models.ManyToManyField("accounts.Profile", related_name="group_chats")


class GroupMessage(models.Model):
    chat = models.ForeignKey("messenger.GroupChat", on_delete=models.CASCADE, related_name="group_messages")
    text = models.TextField(max_length=2048)
    owner = models.ForeignKey("accounts.Profile", on_delete=models.DO_NOTHING, related_name="group_messages")
    pub_date_time = models.DateTimeField(auto_now=True)
