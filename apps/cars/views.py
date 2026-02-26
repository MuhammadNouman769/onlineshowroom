""" ============== IMPORTS =============== """
from wsgiref.util import request_uri
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from .models import ShowRoom, Cars, Review
from .serializers import ShowRoomSerializer, CarModelSerializer, ReviewSerializer
from rest_framework import generics
from rest_framework import mixins
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


""" ============== Start Review View =============== """
class ReviewListCreateView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    @swagger_auto_schema(
        operation_description="Get list of all reviews",
        responses={200: ReviewSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Create a new review",
        request_body=ReviewSerializer(),
        responses={201: ReviewSerializer()}
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
""" ---------------- End Review View ---------------- """


""" ============== Start Review Detail View =============== """
class ReviewDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    """
    GET /all/reviews/<pk>/
            - Retrieve a review.
    PUT /all/reviews/<pk>/
            - Full update.
    PATCH /all/reviews/<pk>/
            - Partial update.
    DELETE /all/reviews/<pk>/
         - Delete a review.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    @swagger_auto_schema(
        operation_description="Get review details by ID",
        responses={200: ReviewSerializer()}
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Full update of review (PUT)",
        request_body=ReviewSerializer(),
        responses={200: ReviewSerializer()}
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Partial update of review (PATCH)",
        request_body=ReviewSerializer(partial=True),
        responses={200: ReviewSerializer()}
    )
    def patch(self, request, *args, **kwrags):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a review",
        responses={204: 'Review deleted successfully'}
    )
    def delete(self, request, *args, ** kwargs):
        return self.destroy(request, *args, **kwargs)


''' ---------------- End Review Detail View ---------------- '''


""" ============== Start ShowRoom Views =============== """
class ShowRoomListCreate(APIView):
   # authentication_classes = [BasicAuthentication]
   # permission_classes = [IsAuthenticated]
   # permission_classes = [AllowAny]
   # persimmion_classes = [IsAdminUser]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
   # persimmion_classes = [IsAdminUser]
   # persimmion_classes = [AllowAny]
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

    """ ---------------- End ShowRoom ListCreate View ---------------- """

""" ============== Start ShowRoom Detail View =============== """
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

""" ---------------- End ShowRoom Detail View ---------------- """


""" ============== Start Car Views =============== """
@swagger_auto_schema(
    method='GET',
    operation_description="Get list of all cars",
    responses={200: CarModelSerializer(many=True)}
)
@swagger_auto_schema(
    method='POST',
    operation_description="Create one or multiple cars",
    request_body=CarModelSerializer(many=True),
    responses={201: CarModelSerializer(many=True)}
)
@api_view(['GET', 'POST'])
def car_list_view(request):
    """
    GET /all/cars/ - List all cars.
    POST /all/cars/ - Create one or multiple cars.
    """
    if request.method == 'GET':
        cars = Cars.objects.all()
        serializer = CarModelSerializer(cars, many=True)
        return Response(serializer.data)

    many = isinstance(request.data, list)
    serializer = CarModelSerializer(data=request.data, many=many)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


""" ---------------- End Car List View ---------------- """

""" ============== Start Car Detail View =============== """

@swagger_auto_schema(
    method='GET',
    operation_description="Retrieve car details by ID",
    responses={200: CarModelSerializer()}
)
@swagger_auto_schema(
    method='PUT',
    operation_description="Full update of car",
    request_body=CarModelSerializer(),
    responses={200: CarModelSerializer()}
)
@swagger_auto_schema(
    method='PATCH',
    operation_description="Partial update of car",
    request_body=CarModelSerializer(partial=True),
    responses={200: CarModelSerializer()}
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
        serializer = CarModelSerializer(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarModelSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = CarModelSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car.delete()
        return Response({'message': 'Car deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    """ ---------------- End Car Detail View ---------------- """