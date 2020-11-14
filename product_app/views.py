from django.shortcuts import render

# Create your views here.
def home(request):
    """Home"""
    return render(request,'products/home.html')