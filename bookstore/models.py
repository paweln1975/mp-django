from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=80, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=50, null=False)
    number1 = models.CharField(name="number", max_length=10, null=False)
    flat = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=50, null=False)

    def full_name(self):
        flat_str = ""
        if self.flat is not None:
            flat_str = f"/{self.flat}"
        return f"{self.street} {self.number}{flat_str} {self.city}"

    def __str__(self):
        return self.full_name()

    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    address = models.OneToOneField(Address, null=True, on_delete=models.SET_NULL, related_name="author")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    published_countries = models.ManyToManyField(Country, related_name="books", blank=True)

    def __str__(self):
        return f"{self.title} (Rating:{self.rating})"

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Review(models.Model):
    user_name = models.CharField(max_length=50, null=False)
    review_text = models.TextField(max_length=400, null=False, validators=[MinLengthValidator(10)])
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


class Profile(models.Model):
    file_name = models.CharField(max_length=500)
    image = models.FileField(upload_to="images")

    def full_name(self):
        return f"{self.file_name} {self.image.name} {self.image.path}"

    def __str__(self):
        return self.full_name()
