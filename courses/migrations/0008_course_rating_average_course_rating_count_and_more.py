# Generated by Django 4.0 on 2022-09-15 17:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('courses', '0007_alter_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='rating_average',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='course',
            name='rating_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='lectures',
            field=models.ManyToManyField(blank=True, to='courses.Lecture'),
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='users_rated',
            field=models.ManyToManyField(blank=True, to='courses.UserRating'),
        ),
    ]
