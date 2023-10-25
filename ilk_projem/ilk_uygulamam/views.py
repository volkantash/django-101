from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    HttpResponse("Merhaba, Dünya. Bu benim ilk projem.")