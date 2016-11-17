from django.shortcuts import render

from .models import Price, Site

# Create your views here.

def home (request):
    return render(request, 'home.html')
def prices(request):
    prices = Price.objects.order_by('price_base')
    return render(request, 'prices.html', {'prices': prices})
def sites(request):
    sites = Site.objects.order_by('date_made')
    return render(request, 'sites.html', {'sites': sites})
