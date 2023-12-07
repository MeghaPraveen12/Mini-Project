from django.contrib import admin
from django.urls import path
from.views import login, register, book, payment, tickets, logout
from.import views 

urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('book',views.book,name="book"),
    path('payment',views.payment,name="payment"),
    path('tickets',views.tickets,name="tickets"),
    path('logout',views.logout,name="logout"),
]