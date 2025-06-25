from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return HttpResponse("<h1>Welcome to Craft Nest - Artisans Meet Buyers</h1>")
