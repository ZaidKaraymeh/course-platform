from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = RichTextField()
    lectures = models.ManyToManyField("courses.Lecture")
    
    price = models.DecimalField(max_digits=4, decimal_places=3)
    coupon = models.IntegerField(default= 0, 
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
            ])

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    @property
    def final_price(self):
        return self.price - self.price * (self.coupon/100)




class Lecture(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    video = models.FileField(upload_to='uploads/%Y/%m/%d/', max_length=100)


    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

