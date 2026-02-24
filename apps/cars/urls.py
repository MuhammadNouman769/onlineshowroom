from django.urls import path
from . import views

urlpatterns = [
    # Cars
    path('cars/', views.car_list_view, name='car_list'),
    path('cars/<int:pk>/', views.car_detail_view, name='car_detail'),

    # ShowRooms
    path('showrooms/', views.ShowRoomListCreate.as_view(), name='showroom_list'),
    path('showrooms/<int:pk>/', views.ShowRoomDetail.as_view(), name='showroom_detail'),
]