from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import Login, Register, Movie, Booking

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies} )

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username, password=password)
        Login_obj=Login(username=username,password=password)
        Login_obj.save()
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            return redirect("register")
    else:
        return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        Register_obj=Register(username=username,email=email,mobile_number=mobile_number,password=password,confirm_password=confirm_password)
        Register_obj.save()
        if password == confirm_password:
            user=User.objects.create_user(username=username, password=password)  
            user.save()
            print('user created')
        else:
            print('Password not matching')

        return redirect('login')
    else:
        return render(request, 'register.html')

@login_required(login_url='login')

def book(request):
    return render(request, 'book.html')

def payment(request):
    return render(request, 'payment.html')

def tickets(request):
    booking = Booking.objects.all()
    return render(request, 'tickets.html',{'booking':booking})

def logout(request):
    auth.logout(request)
    return redirect("/")