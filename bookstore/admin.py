from django.contrib import admin
from .models import Book, Author, Address, Country, Review
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user_name", "rating")


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("title", "author", "rating", "is_bestselling")
    list_display = ("id", "title", "rating")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "number", "flat", "city")


class CountryAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Review, ReviewAdmin)