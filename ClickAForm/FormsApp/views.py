from django.shortcuts import render
from django.http import HttpResponse

def HomePage(request):
    return HttpResponse("Hello, World!")
