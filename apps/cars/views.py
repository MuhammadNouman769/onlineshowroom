from django.shortcuts import render
from .models import Cars,ShowRoom
from django.http import JsonResponse
from django.http import HttpResponse
import json
from .serializers import CarSerializer,ShowRoomSerializer
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404


class Showroom_view(APIView):

    def get(self, request):
        shoowroom = ShowRoom.objects.all()
        serializer = ShowRoomSerializer(shoowroom, many=True)
        return Response(serializer.data)

    def post(self, request):
        many = isinstance(request.data, list)
        serializer = ShowRoomSerializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




''' ------------- Serializers Api get objects list --------------- '''
@api_view(['GET', 'POST'])
def car_list_view(request):
    if request.method == 'GET':
        car = Cars.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


''' ------------- Signal object api --------------- '''

@api_view(['GET', 'PUT', 'DELETE'])
def car_detail_view(request, pk):
    if request.method == 'GET':
        try:
            car = Cars.objects.get(pk=pk)
        except:
            return Response({'Error':'No Car Found'},status=status.HTTP_404_NOT_FOUND)
        car = Cars.objects.get(pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    if request.method == 'PUT':
        car = Cars.objects.get(pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        car = Cars.objects.get(pk=pk)
        car.delete()
        return Response({'message':'Car Delete successfully'},status=status.HTTP_204_NO_CONTENT)
    else:
        car = Cars.objects.get(pk=pk)
















'''------------- ManualApiView --------------'''
'''
def car_list(request):
    cars = Cars.objects.all()
    data = {
        'cars':list(cars.values()),
    }
    
    data_json = json.dumps(data)
    return HttpResponse(data_json, content_type='application/json')
  #  return JsonResponse(data)

def car_detail(request, pk):
    car = Cars.objects.get(pk=pk)
    data = {
        'name':car.name,
        'description':car.description,
        'active':car.active
    }
    return JsonResponse(data)
    '''
