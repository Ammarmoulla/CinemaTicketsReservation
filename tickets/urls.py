from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
import uuid

router = DefaultRouter()
router.register('guests', views.GuestViewset)
router.register('movies', views.MovieViewset)
router.register('reservations', views.ReservationViewset)

urlpatterns = [
    #1
    path('django/jsonresponsenomodel/', views.no_rest_no_model),

    #2 
    path('django/jsonresponsefrommodel/', views.no_rest_from_model),
    
    #3.1 GET POST from rest framework function based view @api_view
    path('rest/fbv/', views.FBV_List),

    #3.2 GET PUT DELETE from rest framework function based view @api_view
    path('rest/fbv/<uuid:pk>', views.FBV_pk),

    #4.1 GET POST from rest framework class based view APIView
    path('rest/cbv/', views.CBV_List.as_view()),

    #4.2 GET PUT DELETE from rest framework class based view APIView
    path('rest/cbv/<uuid:pk>', views.CBV_pk.as_view()),

    #5.1 GET POST from rest framework class based view mixins
    path('rest/mixins/', views.mixins_list.as_view()),

    #5.2 GET PUT DELETE from rest framework class based view mixins
    path('rest/mixins/<uuid:pk>', views.mixins_pk.as_view()),

    #6.1 GET POST from rest framework class based view generics
    path('rest/generics/', views.generics_list.as_view()),

    #6.2 GET PUT DELETE from rest framework class based view generics
    path('rest/generics/<uuid:pk>', views.generics_pk.as_view()),
    
    #7 Viewsets
    path('rest/viewsets/', include(router.urls)),

    #8 find movie 
    path('fbv/findmovie', views.find_movie),

    #9 new reservation
    path('fbv/newreservation',views.new_reservation),

]