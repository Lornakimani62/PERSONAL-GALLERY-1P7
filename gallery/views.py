from django.shortcuts import render
from .models import Location,Category,Image

# Create your views here.
def home(request):
    images = Image.get_all_images()
    title = 'Gallery Home'
    return render(request,'index.html',{'title':title, 'images':image})

def image(request):

    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()

    return render(request,'details.html',{"image":image})

def search(request):

    return render(request,'search.html')