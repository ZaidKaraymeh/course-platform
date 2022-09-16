from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

def home(request):
    courses = Course.objects.all()
    context = {
        'courses':courses
    }
    return render(request, 'home.html', context)


def course(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {
        'course':course
    }
    return render(request, 'course.html', context)



