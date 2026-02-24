from django.urls import path
from . import views

urlpatterns = [
    #path('', views.car_list, name='car_list'),
    path('cars/', views.car_list_view,name='car_list'),
    path('cars/<int:pk>/', views.car_detail_view, name='car_detail'),
    path('showroom/', views.Showroom_view.as_view(), name='showroom'),
    path('showroom/<int:pk>/', views.showroom_detail.as_view(), name='car_detail')
]
