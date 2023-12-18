from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

# Create your views here.

def SearchResult(rewuest):
    products=None
    query=None
    if 'q' in rewuest.GET:
        query=rewuest.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query) )
        return render(rewuest,'search.html',{'query':query,'products':products})

