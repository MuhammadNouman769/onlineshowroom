from django.urls import path
from . import views

urlpatterns = [
    #path('', views.car_list, name='car_list'),
    path('cars/', views.car_list_view,name='car_list'),
    path('<int:pk>/', views.car_detail_view, name='car_detail'),
    path('showroom/', views.Showroom_view.as_view(), name='showroom'),
  #  path('<int:pk>/', views.car_detail, name='car_detail')
]
