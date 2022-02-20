from django.contrib import admin
from .models import Tag, Author, Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("post_date", "author", "tags")
    list_display = ("id", "title", "author", "post_date")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_email", "post")


admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)