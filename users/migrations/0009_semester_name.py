# Generated by Django 3.2.9 on 2022-03-25 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
