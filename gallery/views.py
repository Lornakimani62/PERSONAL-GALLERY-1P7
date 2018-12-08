from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,'index.html')

def image(request):

    return render(request,'details.html')

def search(request):

    return render(request,'search.html')