from django.contrib import admin
from django.contrib.auth.models import User

from .models import Profile


# Register your models here.

@admin.register(Profile)
class ProfileInline(admin.ModelAdmin):
    pass

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass
