from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Movie, Guest, Reservation
from .serializers import MovieSerializer, GuestSerializer, ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
# Create your views here.


def no_rest_no_model(request):
    guests = [
        {
           "id": 1,
           "name": "Ahmad Ali",
           "mobile": "0997125656",
        },

        {
           "id": 2,
           "name": "Alaa Moulla",
           "mobile": "0991801722",
        }
    ]

    return JsonResponse(guests, safe=False)


def no_rest_from_model(request):
    gusets = Guest.objects.all()
    response = {
        "guests": list(gusets.values("name", "mobile"))
        }
    return JsonResponse(response) 

@api_view(['GET', 'POST'])
def FBV_List(request):
    
    if request.method == "GET":
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def FBV_pk(request, pk):
    
    guest = get_object_or_404(Guest, id=pk)

    if request.method == "GET":
        serializer = GuestSerializer(guest)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        guest.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    
class CBV_List(APIView):
    
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CBV_pk(APIView):
    def get_object(self, pk):
        return get_object_or_404(Guest, id=pk)
    
    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class mixins_list(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView
):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class mixins_pk(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request)
    
    def delete(self, request, pk):
        return self.destroy(request)

class generics_list(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class GuestViewset(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]


class ReservationViewset(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


@api_view(['GET'])
def find_movie(request):
    movie = Movie.objects.filter(
        movie=request.data["movie"]
    )
    serializer = MovieSerializer(movie, many=True)  
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def new_reservation(request):
    
    guest = Guest.objects.create(
            name=request.data["name"],
            mobile=request.data["mobile"],
        )
    movie = Movie.objects.get(
            movie=request.data["movie"],
            hall=request.data["hall"]
        )

    reservation = Reservation.objects.create(
            movie=movie,
            guest=guest
        )

    return Response(status=status.HTTP_201_CREATED)