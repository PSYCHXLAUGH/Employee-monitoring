from django.db import models


class Booking(models.Model):
    booking_date = models.DateField()
    comment = models.TextField()
    number_of_people = models.IntegerField()
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)


class Table(models.Model):
    table_number = models.IntegerField(primary_key=True)
    seats_available = models.IntegerField()
    status = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)


class Address(models.Model):
    location = models.CharField(max_length=50)