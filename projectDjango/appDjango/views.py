from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    items = Item.objects.all()
    context = {"items_value": items}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')