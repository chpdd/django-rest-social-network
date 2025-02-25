from django.contrib import admin

from .models import Post, Comment

@admin.register(Post)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass