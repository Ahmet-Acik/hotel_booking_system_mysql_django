# filepath: /Users/drahmetacik/Projects/hotel_bs_mysql_django/hotel_booking_system/bookings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Guest URLs
    path('guests/', views.guest_list, name='guest_list'),
    path('guests/new/', views.guest_create, name='guest_create'),
    path('guests/<int:pk>/edit/', views.guest_update, name='guest_update'),
    path('guests/<int:pk>/delete/', views.guest_delete, name='guest_delete'),

    # Room URLs
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/new/', views.room_create, name='room_create'),
    path('rooms/<int:pk>/edit/', views.room_update, name='room_update'),
    path('rooms/<int:pk>/delete/', views.room_delete, name='room_delete'),

    # Booking URLs
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/new/', views.booking_create, name='booking_create'),
    path('bookings/<int:pk>/edit/', views.booking_update, name='booking_update'),
    path('bookings/<int:pk>/delete/', views.booking_delete, name='booking_delete'),

    # Payment URLs
    path('payments/', views.payment_list, name='payment_list'),
    path('payments/new/', views.payment_create, name='payment_create'),
    path('payments/<int:pk>/edit/', views.payment_update, name='payment_update'),
    path('payments/<int:pk>/delete/', views.payment_delete, name='payment_delete'),

    # Service URLs
    path('services/', views.service_list, name='service_list'),
    path('services/new/', views.service_create, name='service_create'),
    path('services/<int:pk>/edit/', views.service_update, name='service_update'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),
]