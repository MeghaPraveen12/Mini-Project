from django.contrib import admin
from .models import Register, Login, Movie, Screen, Booking, Seat

# Register your models here.

admin.site.register(Register)
admin.site.register(Login)
admin.site.register(Movie)
admin.site.register(Screen)
admin.site.register(Booking)
admin.site.register(Seat)