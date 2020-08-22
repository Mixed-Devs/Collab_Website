from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class TestPageView(TemplateView):
    template_name = 'test.html'

class BasePageView(TemplateView):
    template_name = 'base.html'

class Daniilwebsite(TemplateView):
    template_name = 'daniil_website.html'