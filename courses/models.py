from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null = True, default='default.jpg')

    lectures = models.ManyToManyField("courses.Lecture", blank=True)
    
    price = models.DecimalField(max_digits=6, decimal_places=3)
    coupon = models.IntegerField(default= 0, 
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
            ])

    """
        Calculate Average
        ((n)*old_average + new_rating )/(n+1)
        increment n
    """
    rating_average = models.DecimalField(max_digits=2, decimal_places=1, default=0,
        validators=[
                MaxValueValidator(5),
                MinValueValidator(0)
                ])
    rating_count = models.IntegerField(default= 0)

    """
        Check if user found in users_rated, 
        if user not in users_rated, 
            call add_new_average
            increment rating_count
            update rating_average
        else:
            get old rating
            call subtract_new_average
            decrement rating_count
            update rating_average

            call add_new_average with new value
            increment rating_count
            update rating_average

    """

    users_rated = models.ManyToManyField("courses.UserRating", blank=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    @property
    def final_price(self):
        return round(self.price - self.price * Decimal(self.coupon/100), 3)

    def __str__(self):
        return self.title
    


class UserRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[
                MaxValueValidator(5),
                MinValueValidator(0)
                ])




class Lecture(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    video = models.FileField(upload_to='uploads/%Y/%m/%d/', max_length=100)


    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

