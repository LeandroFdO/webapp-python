from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, "menu/home.html")

def results(request, nome):
    return HttpResponse(response % nome)

