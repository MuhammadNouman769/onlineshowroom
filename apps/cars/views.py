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
from django.shortcuts import get_object_or_404

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

    # GET → list all cars
    if request.method == 'GET':
        cars = Cars.objects.all()
        serializer = CarSeriliazer(cars, many=True)
        return Response(serializer.data)

    # POST → single or bulk create
    elif request.method == 'POST':

        is_many = isinstance(request.data, list)
        serializer = CarSeriliazer(data=request.data, many=is_many)

        if serializer.is_valid():
            if is_many:
                cars = [Cars.objects.create(**item) for item in serializer.validated_data]
                return Response(CarSeriliazer(cars, many=True).data,
                                status=status.HTTP_201_CREATED)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''------------- Signal object api ---------------'''

@api_view(['GET', 'PUT', 'DELETE'])
def car_detail_view(request, pk):

    car = get_object_or_404(Cars, pk=pk)

    # GET
    if request.method == 'GET':
        serializer = CarSeriliazer(car)
        return Response(serializer.data)

    # UPDATE
    elif request.method == 'PUT':
        serializer = CarSeriliazer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)