from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'name':'Surendra Giri',
        'Age':20
    }
    # return HttpResponse("This is Home Page")
    return render(request, "index.html", context)

def about(request):
    return HttpResponse("Hello, This Is About page")

def contact(request):
    return HttpResponse("Hello, This Is Contact page")