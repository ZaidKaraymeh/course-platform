# Generated by Django 4.0 on 2022-09-19 11:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_alter_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
