from django.shortcuts import render
from .models import Location,Category,Image

# Create your views here.
def home(request):
    images = Image.get_all_images()
    title = 'Gallery Home'
    return render(request,'index.html',{'title':title, 'images':images})

def image(request,image_id):

    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()

    return render(request,'details.html',{"image": image})

def search(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

    return render(request,'search.html')