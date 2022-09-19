from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('view/<str:course_id>', views.course, name="course"),
    path('cart/<str:course_id>', views.cart, name="add_to_cart"),
    path('cart/', views.cart, name="cart"),
    path('orders/', views.orders, name="orders"),
    path('checkout/', views.checkout, name="checkout"),

]