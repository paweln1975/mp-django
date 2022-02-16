# Generated by Django 3.2.11 on 2022-02-16 23:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0009_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_text',
            field=models.TextField(max_length=400, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
