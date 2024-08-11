from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    list_display = ['author', 'post']
