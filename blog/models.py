from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    e_mail = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20, null=False)

    def full_name(self):
        return f"{self.caption}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    excerpt = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to="images", null=True)
    post_date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True, unique=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    content = models.TextField(validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def full_name(self):
        return f"{self.title}"

    def __str__(self):
        return self.full_name()

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.slug])


class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
