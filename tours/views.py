from django.shortcuts import render
from django.views import generic


class ToursList(generic.TemplateView):
    template_name = 'tours_list.html'
