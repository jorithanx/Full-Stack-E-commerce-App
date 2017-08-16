from django.shortcuts import render

from products.models import Product

from .models import SearchQuery


def searches(request):
   query = request.GET.get('q', "")
   user = None
   if request.user.is_authenticated:
      user = request.user
   context = {"query": query}
   if query is not "":
      SearchQuery.objects.create(user=user, query=query)
      product_list = Product.objects.search(query=query)
      context['product_list'] = product_list
   return render(request, 'search.html', context)
