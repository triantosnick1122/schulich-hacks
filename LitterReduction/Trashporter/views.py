from django.shortcuts import render
from django.http import HttpResponse
import json

def index(request):
    return render(request, "index.html")

def litter_map(request): 
    # Your code to retrieve the location and other data goes here
    locations = [(30.5, 50.5), (30.55, 50.6)]
    descriptions = ["This is a description of the location", "second description"]
    
    return render(request, 'map.html', {'locations': json.dumps(locations), 'descriptions': json.dumps(descriptions)})
