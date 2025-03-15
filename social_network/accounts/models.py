from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, max_length=512)


class Subscription(models.Model):
    subscriber = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="subscriptions")
    subscribed_to = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="subscriptions_to_me")

    class Meta:
        unique_together = ["subscriber", "subscribed_to"]


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
