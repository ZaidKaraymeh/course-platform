from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

# Create your views here.

def home(request):
    courses = Course.objects.all()
    context = {
        'courses':courses
    }
    return render(request, 'home.html', context)

"""
    View a Course
"""
def course(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {
        'course':course
    }
    return render(request, 'course.html', context)
"""
    View Purchased Courses
"""
def courses(request, course_id=''):
    user = request.user
    context = {
    }
    
    try:
        if course_id != '' and Course.objects.filter(id=course_id).exists() :
            course = PurchasedCourse.objects.get(user = user, course=course_id)
            context['course'] = course
            return render(request, 'learn.html', context)
    except Exception:
        return redirect('courses')

    courses = PurchasedCourse.objects.filter(user=user)
    context['courses'] = courses
    return render(request, 'courses.html', context)

def lectures(request, course_id=''):
    user = request.user
    context = {
    }
    if Course.objects.filter(id=course_id).exists() and PurchasedCourse.objects.filter(user=user, course=course_id).exists():
        course = Course.objects.get(id=course_id)
        
        context['course'] = course

        return render(request, 'lectures.html', context)

    return redirect('courses')

def learn(request, course_id='', lecture_id=''):
    user = request.user
    context = {
    }

    if not PurchasedCourse.objects.filter(user=user, course=course_id).exists():
        return render('courses')

    course = Course.objects.get(id=course_id)
    lecture = Lecture.objects.get(id=lecture_id)

    context['course'] = course
    context['lecture'] = lecture

    return render(request, 'learn.html', context)

def cart(request, course_id=''):
    user = request.user
    cart, created = Cart.objects.get_or_create(
        user = user,
    )
    context = {
        'user':user,
        'cart':cart
    }
    if request.method == "POST" and course_id != '':

        course = Course.objects.get(id=course_id)
        if course in cart.courses.all():
            messages.error(request, f"{course.title} already in cart")
            return redirect('course', course_id)


        cart.courses.add(course)
        cart.price += course.final_price
        cart.save()

        messages.success(request, f"{course.title} added to cart")
        return redirect('course', course_id)
    #if request.method == "GET":
    return render(request, 'cart.html', context)


"""
    Recieves request from 'cart', adds a PurchasedCourse record to all items in cart
    makes Reciept object identical to cart
    clears cart price and courses

"""

def checkout(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(
        user = user,
    )

    for course in cart.courses.all():
        purchased_course = PurchasedCourse.objects.create(
            user= user,
            course = course,
            price = course.final_price
        )
        purchased_course.save()

    reciept = Reciept.objects.create(
        user=user,
        price = cart.price,
    )
    reciept.save()
    reciept.courses.set(cart.courses.all())
    cart.courses.clear()
    cart.price = 0.00
    cart.save()
    messages.success(request, f"Purchase Complete")
    return redirect('orders')

def orders(request):
    user = request.user
    orders = PurchasedCourse.objects.filter(user=user).order_by('-created_at')

    context = {
        'orders':orders
    }

    return render(request, 'orders.html', context)
