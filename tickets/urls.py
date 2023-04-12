from django.urls import path, include
from . import views

urlpatterns = [
    #1
    path('django/jsonresponsenomodel/', views.no_rest_no_model),

    #2 
    path('django/jsonresponsefrommodel/', views.no_rest_from_model),
    
    #3.1 GET POST from rest framework function based view @api_view
    path('rest/fbv/', views.FBV_List),

    #3.2 GET PUT DELETE from rest framework function based view @api_view
    path('rest/fbv/<int:pk>', views.FBV_pk),

    #4.1 GET POST from rest framework class based view APIView
    #path('rest/cbv/', views.CBV_List.as_view()),

    #4.2 GET PUT DELETE from rest framework class based view APIView
    #path('rest/cbv/<int:pk>', views.CBV_pk.as_view()),


]