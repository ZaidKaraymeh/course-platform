# Generated by Django 4.0 on 2022-09-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_alter_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='video',
            field=models.FileField(default='default_lecture.mp4', upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
