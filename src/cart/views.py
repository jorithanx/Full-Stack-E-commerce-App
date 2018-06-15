from django.shortcuts import render, redirect
from django.contrib import messages

def cart_page(request):
   """
   A view that renders the cart contents page
   """
   return render(request, "cart.html")


def add_to_cart(request, id):
   """
   Add a quantity of the specified product to the cart
   """

   if request.method == 'POST':
      quantity = int(request.POST['quantity'])

      cart = request.session.get('cart', {})

      string_id = str(id)

      if string_id in cart:
         cart[string_id] = int(cart[string_id]) + quantity  
      else:
         cart[id] = cart.get(id, quantity)

      request.session['cart'] = cart
      messages.success(request, "You have added the product to your cart!")

      return redirect(request.META['HTTP_REFERER'])


def edit_cart(request, id):
   """
   Edit the quantity of the specified product to the specified amount
   """
   quantity = int(request.POST['quantity'])
   cart = request.session.get('cart', {})

   if quantity > 0:
      cart[id] = quantity
   else:
      cart.pop(str(id))

   request.session['cart'] = cart

   return redirect('cart')


def remove_item_cart(request, id):
   """
   Remove the whole specified product from the cart
   """
   quantity = int(request.POST['remove'])
   cart = request.session.get('cart', {})
   cart.pop(str(id))
   request.session['cart'] = cart

   return redirect('cart')


# hobby-session-41
