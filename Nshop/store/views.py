from django.shortcuts import render

def home(request):
    return render(request,"store/index.html")

# Create your views here.
