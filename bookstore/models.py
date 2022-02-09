from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    author = models.CharField(max_length=100, null=True)
    is_bestselling = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} {self.rating}"

