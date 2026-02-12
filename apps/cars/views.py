from django.shortcuts import render
from .models import Cars
from django.http import JsonResponse
from django.http import HttpResponse
import json
from .serializers import CarSeriliazer
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework.decorators import api_view

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

@api_view()
def car_detail_view(request, pk):
    car = Cars.objects.get(pk=pk)
    serializer = CarSeriliazer(car)
    return Response(serializer.data)
        