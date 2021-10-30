from django.urls import path, include
from .views import *


app_name = 'tours'
urlpatterns = [
    path('', ToursListView.as_view(),name ='tours-list'),
    path('<int:pk>/', ToursDetailView.as_view(),name ='tour-detail'),
    
    
    
]