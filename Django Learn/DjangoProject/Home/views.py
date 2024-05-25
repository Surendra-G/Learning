from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is Home Page")

def about(request):
    return HttpResponse("Hello, This Is About page")

def contact(request):
    return HttpResponse("Hello, This Is Contact page")