from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,"home.html")

def catalog(request):
    return render(request,"catalog.html")

def product_detail(request):
    return render(request,"product_detail.html")