from django.urls import path
from .views import UserListCreateView, HotelListCreateView, RoomListCreateView, BookingListCreateView

app_name = "core"

urlpatterns = [
    path("users/", UserListCreateView.as_view(), name="users"),
    path("hotels/", HotelListCreateView.as_view(), name="hotels"),
    path("rooms/", RoomListCreateView.as_view(), name="rooms"),
    path("bookings/", BookingListCreateView.as_view(), name="bookings"),
]
