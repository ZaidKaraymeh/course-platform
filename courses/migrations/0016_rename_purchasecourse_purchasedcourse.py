# Generated by Django 4.0 on 2022-09-19 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('courses', '0015_purchasecourse_reciept_cart_price_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PurchaseCourse',
            new_name='PurchasedCourse',
        ),
    ]
