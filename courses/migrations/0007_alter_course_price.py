# Generated by Django 4.0 on 2022-09-15 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_lecture_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]
