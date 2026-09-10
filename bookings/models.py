from django.db import models
class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    event_date = models.CharField(max_length=100)
    hall_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

# Create your models here.
