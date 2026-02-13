from django.shortcuts import render
from .models import Cars
from django.http import JsonResponse
from django.http import HttpResponse
import json
from .serializers import CarSeriliazer
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework.decorators import api_view
from rest_framework import status

'''------------- Manual Api View --------------'''
def car_list(request):
    cars = Cars.objects.all()
    data = {
        'cars':list(cars.values()),
    }
    ''' convert data into json response '''
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
    
''' ------------- Serializers Api get objects list --------------- '''

@api_view(['GET', 'POST'])
def car_list_view(request):
    if request.method == 'GET':
        try:
            cars = Cars.objects.all()
        except:
            return Response({'error': 'No cars found'})
        car = Cars.objects.all()
        serializer = CarSeriliazer(car, many=True)
        return Response(serializer.data)
            
    if request.method == 'POST':
        serializer = CarSeriliazer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    return None

'''------------- Signal object api ---------------'''

@api_view(['GET', 'POST','DELETE'])
def car_detail_view(request, pk):
    if request.method == 'GET':
        car = Cars.objects.get(pk=pk)
        serializer = CarSeriliazer(car)
        return Response(serializer.data)
    if request.method == 'PUT':
        car = Cars.objects.get(pk=pk)
        serializer = CarSeriliazer(car,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        if request.method == 'DELETE':
            car = Cars.objects.get(pk=pk)
            car.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

