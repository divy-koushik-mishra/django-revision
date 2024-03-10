from django.shortcuts import render, HttpResponse
# from django import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse("Check maadi!!")
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("Check maadi!!")
    return render(request, 'about.html')
