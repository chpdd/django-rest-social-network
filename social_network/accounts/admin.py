from django.contrib import admin

from .models import User, Profile


# Register your models here.
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
