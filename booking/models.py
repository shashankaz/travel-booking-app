from django.db import models
from django.contrib.auth.models import User

# Travel Options Model
class TravelOption(models.Model):
    TYPE_CHOICES = [('Flight', 'Flight'), ('Train', 'Train'), ('Bus', 'Bus')]
    travel_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.IntegerField()

    def __str__(self):
        return f'{self.travel_type} from {self.source} to {self.destination}'

# Booking Model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
    number_of_seats = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')])

    def __str__(self):
        return f'Booking {self.pk} - {self.status}'
