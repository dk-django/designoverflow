from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView 


class HomepageView(TemplateView):
    template_name = 'generator/homepage.html'