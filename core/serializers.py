from rest_framework import serializers, viewsets
from .models import Hotel, Room, Booking
from django.contrib.auth import get_user_model

User =  get_user_model()
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    hotel_name = serializers.CharField(source='hotel.name', read_only=True)

    class Meta:
        model = Room
        fields = ('id', 'name', 'description', 'price', 'image', 'hotel', 'hotel_name')


class BookingSerializer(serializers.ModelSerializer):
    room_name = serializers.CharField(source='room.name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Booking
        fields = ('id', 'room', 'room_name', 'user', 'user_email', 'check_in_date',
                  'check_out_date', 'num_guests', 'created_at', 'updated_at', 'is_paid', 'discount')
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'username', 'last_name', 'password', 'email')
