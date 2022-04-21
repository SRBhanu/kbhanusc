from django.shortcuts import render
from shop.models import product
from django.db.models import Q  # importing Q objects to provide search functionality to the site



def searchResult(request):
    products =None
    query = None
    if 'q' in request.GET:  # checking if there is a search request
        query = request.GET.get('q')
        products = product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))  # searching products by queries
    return render(request, 'search.html', {'query': query, 'products': products})
