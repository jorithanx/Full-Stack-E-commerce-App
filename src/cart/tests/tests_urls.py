from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cart.views import (
   cart_page,
   add_to_cart,
   edit_cart
   )

class TestUrls(SimpleTestCase):
   def test_cart_checkout_url_is_resolved(self):
      url = reverse("cart")
      self.assertEqual(resolve(url).func, cart_page)

   def test_add_to_cart_cart_checkout_url_is_resolved(self):
      url = reverse("add-to-cart", args=[1])
      self.assertEqual(resolve(url).func, add_to_cart)
   
   def test_edit_cart_cart_checkout_url_is_resolved(self):
      url = reverse("edit-cart", args=[1])
      self.assertEqual(resolve(url).func, edit_cart)