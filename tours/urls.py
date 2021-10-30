from django.urls import path, include
from .views import ToursList


app_name = 'tours'
urlpatterns = [
    path('', ToursList.as_view(),name ='tours-list'),
    
]