# Generated by Django 4.0 on 2022-09-15 09:59

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', ckeditor.fields.RichTextField()),
                ('video', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='section',
            name='articles',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='body',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='course',
            name='sections',
        ),
        migrations.AddField(
            model_name='course',
            name='coupon',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.AddField(
            model_name='course',
            name='lectures',
            field=models.ManyToManyField(to='courses.Lecture'),
        ),
    ]
