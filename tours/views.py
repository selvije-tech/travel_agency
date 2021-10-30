from django.shortcuts import render
from django.views import generic
from .models import *



class LandingPageView(generic.TemplateView):
    template_name = 'landing_page.html'


class ToursListView(generic.ListView):
    template_name = 'tours_list.html'
    queryset = Trip.objects.all()
    context_object_name = 'trips'


class ToursDetailView(generic.DetailView):
    template_name = 'tour_detail.html'
    queryset = Trip.objects.all()
    context_object_name = 'trip'