from rest_framework import serializers, viewsets
from .models import Hotel, Room, Booking
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


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


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.context.get('request', None)
        return context

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.instance
        if not user.check_password(value):
            raise serializers.ValidationError({"message": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance
