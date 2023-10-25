from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Merhaba, Dünya. Bu benim ilk projem.")