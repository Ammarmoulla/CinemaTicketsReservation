from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Movie, Guest, Reservation
from .serializers import MovieSerializer, GuestSerializer, ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
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