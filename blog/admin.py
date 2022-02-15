from django.contrib import admin
from .models import Tag, Author, Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("title", "author")
    list_display = ("id", "title", "author", "post_date")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)


admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
