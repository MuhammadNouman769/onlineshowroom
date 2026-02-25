""" ============== IMPORTS =============== """

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from .models import ShowRoom, Cars
from .serializers import ShowRoomSerializer, CarSerializer


# ---------------- ShowRoom APIs ----------------

class ShowRoomListCreate(APIView):
    """
    GET /all/showrooms/
        - Returns list of all showrooms.
    POST /all/showrooms/
        - Create one or multiple showrooms.
    """

    @swagger_auto_schema(
        operation_description="Get all showrooms",
        responses={200: ShowRoomSerializer(many=True)}
    )
    def get(self, request):
        showrooms = ShowRoom.objects.all()
        serializer = ShowRoomSerializer(showrooms, many=True, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create one or multiple showrooms",
        request_body=ShowRoomSerializer(many=True),
        responses={201: ShowRoomSerializer(many=True)}
    )
    def post(self, request):
        many = isinstance(request.data, list)
        serializer = ShowRoomSerializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowRoomDetail(APIView):
    """
    GET /all/showrooms/<pk>/ - Retrieve a showroom.
    PUT /all/showrooms/<pk>/ - Full update.
    PATCH /all/showrooms/<pk>/ - Partial update.
    DELETE /all/showrooms/<pk>/ - Delete showroom.
    """

    def get_object(self, pk):
        return ShowRoom.objects.get(pk=pk)

    @swagger_auto_schema(
        operation_description="Get showroom details by ID",
        responses={200: ShowRoomSerializer()}
    )
    def get(self, request, pk):
        try:
            showroom = self.get_object(pk)
        except ShowRoom.DoesNotExist:
            return Response({'error': 'No Showroom Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ShowRoomSerializer(showroom)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Full update of showroom (PUT)",
        request_body=ShowRoomSerializer(),
        responses={200: ShowRoomSerializer()}
    )
    def put(self, request, pk):
        try:
            showroom = self.get_object(pk)
        except ShowRoom.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ShowRoomSerializer(showroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partial update of showroom (PATCH)",
        request_body=ShowRoomSerializer(partial=True),
        responses={200: ShowRoomSerializer()}
    )
    def patch(self, request, pk):
        try:
            showroom = self.get_object(pk)
        except ShowRoom.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ShowRoomSerializer(showroom, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a showroom",
        responses={204: 'Showroom deleted successfully'}
    )
    def delete(self, request, pk):
        try:
            showroom = self.get_object(pk)
        except ShowRoom.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        showroom.delete()
        return Response({'message': 'Showroom deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# ---------------- Car APIs ----------------

@swagger_auto_schema(
    method='GET',
    operation_description="Get list of all cars",
    responses={200: CarSerializer(many=True)}
)
@swagger_auto_schema(
    method='POST',
    operation_description="Create one or multiple cars",
    request_body=CarSerializer(many=True),
    responses={201: CarSerializer(many=True)}
)
@api_view(['GET', 'POST'])
def car_list_view(request):
    """
    GET /all/cars/ - List all cars.
    POST /all/cars/ - Create one or multiple cars.
    """
    if request.method == 'GET':
        cars = Cars.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    many = isinstance(request.data, list)
    serializer = CarSerializer(data=request.data, many=many)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='GET',
    operation_description="Retrieve car details by ID",
    responses={200: CarSerializer()}
)
@swagger_auto_schema(
    method='PUT',
    operation_description="Full update of car",
    request_body=CarSerializer(),
    responses={200: CarSerializer()}
)
@swagger_auto_schema(
    method='PATCH',
    operation_description="Partial update of car",
    request_body=CarSerializer(partial=True),
    responses={200: CarSerializer()}
)
@swagger_auto_schema(
    method='DELETE',
    operation_description="Delete a car",
    responses={204: 'Car deleted successfully'}
)
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def car_detail_view(request, pk):
    """
    GET /all/cars/<pk>/ - Retrieve a car.
    PUT /all/cars/<pk>/ - Full update.
    PATCH /all/cars/<pk>/ - Partial update.
    DELETE /all/cars/<pk>/ - Delete a car.
    """
    try:
        car = Cars.objects.get(pk=pk)
    except Cars.DoesNotExist:
        return Response({'error': 'No Car Found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car.delete()
        return Response({'message': 'Car deleted successfully'}, status=status.HTTP_204_NO_CONTENT)