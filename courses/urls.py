from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('view/<str:course_id>', views.course, name="course"),

]