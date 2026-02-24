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

class showroom_detail(APIView):

    def get(self, request, pk):
        showroom = get_object_or_404(ShowRoom, pk=pk)
        serializer = ShowRoomSerializer(showroom)
        return Response(serializer.data)

    def put(self, request, pk):
        showroom = get_object_or_404(ShowRoom, pk=pk)
        serializer = ShowRoomSerializer(showroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        showroom = get_object_or_404(ShowRoom, pk=pk)
        showroom.delete()
        return Response(
            {'message': 'Showroom deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )
    def patch(self, request, pk):
        showroom = get_object_or_404(ShowRoom, pk=pk)
        serializer = ShowRoomSerializer(showroom, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
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
        many = isinstance(request.data, list)
        serializer = CarSerializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


''' ------------- Signal object api --------------- '''

@api_view(['GET', 'PUT', 'DELETE'])
def car_detail_view(request, pk):
    try:
        car = Cars.objects.get(pk=pk)
    except Cars.DoesNotExist:
        return Response(
            {'error': 'No Car Found'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car.delete()
        return Response(
            {'message': 'Car deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )














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
