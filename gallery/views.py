from django.shortcuts import render
from .models import Location,Category,Image

# Create your views here.
def home(request):
    images = Image.get_all_images()
    return render(request,'index.html')

def image(request):

    return render(request,'details.html')

def search(request):

    return render(request,'search.html')