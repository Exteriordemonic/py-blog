from django.contrib import admin

from blog.models import Commentary, Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner"]
    search_fields = ["title", "owner__username"]


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ["content", "user"]
