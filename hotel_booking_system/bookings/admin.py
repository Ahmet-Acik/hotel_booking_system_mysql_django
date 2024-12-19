from django.contrib import admin

from django.contrib import admin
from .models import Guest, Room, Booking, Payment, Service

admin.site.register(Guest)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Service)