from django.db import models

class Register(models.Model):
    username = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=25,null=False)
    mobile_number = models.IntegerField(null=False)
    password = models.CharField(max_length=25,null=False)
    confirm_password = models.CharField(max_length=25,null=False)

    def __str__(self):
        return self.username

class Login(models.Model):
    username = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=25,null=False)

    def __str__(self):
        return self.username

class Screen(models.Model):
    screename = models.CharField(max_length=100, null=False)    

    def __str__(self):
        return self.screename

class Movie(models.Model):
    screen = models.ForeignKey(Screen,on_delete=models.CASCADE, default="1")
    moviename = models.CharField(max_length=100,null=False)
    image = models.ImageField(upload_to="images",null=False,blank=False)

    def __str__(self):
        return self.moviename
    
class Seat(models.Model):
    seatname = models.CharField(max_length=100, null=False)    

    def __str__(self):
        return self.seatname
    
class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen,on_delete=models.CASCADE, default="1")
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)