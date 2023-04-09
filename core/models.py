from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers




class Hotel(models.Model):
    name = models.CharField(_('name'), max_length=255)
    address = models.CharField(_('address'), max_length=255)
    description = models.TextField(_('description'))
    image = models.ImageField(_('image'), upload_to='hotel_images/')
  
    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(_('name'), max_length=255)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    description = models.TextField(_('description'))
    price = models.DecimalField(_('price'), max_digits=8, decimal_places=2)
    image = models.ImageField(_('image'), upload_to='room_images/')

    def __str__(self):
        return f"{self.hotel.name} - {self.name}"


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False)
    discount = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username} - {self.room.name}"

