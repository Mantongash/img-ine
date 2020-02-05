from django.shortcuts import render
from .models import Image
from django.views.generic import TemplateView, ListView


def home(request):
  images = Image.objects.all()
  return render(request, "landing/home.html", {"images":images})


# Create your views here.


def search_results(request):
    '''
    Method to search by location or category
    '''
    if 'result' in request.GET and request.GET["result"]:
        search_term = request.GET.get("result")
        searched_images = Image.search_by_category(search_term)
       
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message, "images":searched_images})
    # elif 'result' in request.GET and request.GET["result"]:
    #     search_term = request.GET.get("result")
    #     searched_images = Image.search_by_location(search_term)
    #     message = f"{search_term}"    

    #     return render(request, 'search_results.html', {"message":message, "images":searched_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search_results.html', {"message":message})

def category(request, id):
    '''
    Method to search by images or category
    '''
    # categories = Category.get_all_categories()
    images = Image.objects.filter(category__id=id)
    context = {
        "categories":categories,
        "images":images
    }
    return render(request, 'search_results.html', context)