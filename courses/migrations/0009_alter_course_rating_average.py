# Generated by Django 4.0 on 2022-09-15 17:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_rating_average_course_rating_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='rating_average',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
