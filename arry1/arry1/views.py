from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("<h1>Home Page</h1>") 
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return HttpResponse("<h1>Contact Page</h1>") 

def service(request):
    return HttpResponse("<h1>Service Page</h1>") 

def blog(request):
    return HttpResponse("<h1>Blog Page</h1>") 