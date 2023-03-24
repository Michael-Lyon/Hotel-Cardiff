from django.shortcuts import render
from django.contrib.auth import get_user_model, login
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from .models import Hotel, Booking, Room
from .serializers import BookingSerializer, HotelSerializer, RoomSerializer, UserSerializer
User = get_user_model()

# Create your views here.

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HotelListCreateView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
 
    def perform_create(self, serializer):
        data = serializer.validated_data
        discount = data['discount']
        user = data['user']
        room = data['room']
        
        # if this user hasn't booked before give him a discount 
        if not Booking.objects.filter(user=user).exists():
            # give a some discount 10%
            discount = (room.price * 0.01)
            serializer.save(discount=discount)
        serializer.save()        
        
        
        
                        
    
    