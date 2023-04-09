from django.urls import path
from .views import UserListCreateView, HotelListCreateView, RoomListCreateView, BookingListCreateView, UserDetailView, HotelDetailView, BookingDetailView, RoomDetailView, ChangePasswordView, home

app_name = "core"

urlpatterns = [
    
    path("", home, name="home"),
    path("users/", UserListCreateView.as_view(), name="users"),
    path("user/<str:username>/", UserDetailView.as_view(), name="user_detail"),
    path("hotels/", HotelListCreateView.as_view(), name="hotels"),
    path("hotel/<int:pk>/", HotelDetailView.as_view(), name="hotel_detail"),
    path("rooms/", RoomListCreateView.as_view(), name="rooms"),
    path("room/<int:pk>/", RoomDetailView.as_view(), name="room_detail"),
    path("bookings/", BookingListCreateView.as_view(), name="bookings"),
    path("bookings/<int:pk>/", BookingDetailView().as_view(), name="bookings_detail"),
    path("change-password/", ChangePasswordView.as_view(), name="Change Password"),
]

