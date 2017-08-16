from django.shortcuts import render

def home_page(request):
   """
   A view that renders the home contents page
   """
   return render(request, "home.html", {})
