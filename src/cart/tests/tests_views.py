from django.test import TestCase
from django.urls import reverse, resolve
from products.models import Product

class TestView(TestCase):
   def setUp(self):
      self.cart = reverse("cart")
      self.add_to_cart = reverse("add-to-cart", args=["1"])
      self.edit_cart = reverse("edit-cart", args=["1"])

      self.kick_scooter_01 = Product.objects.create(
         title="Kick Scooter Example",
         slug="kick-scooter-01",
         stock=10,
         price=150,
      )

   def test_get_cart_page(self):
      page = self.client.get(self.cart)
      self.assertEqual(page.status_code, 200)
      self.assertTemplateUsed(page, 'cart.html')

   def test_add_to_cart_POST(self):
      page = self.client.post(self.add_to_cart, {
         "quantity": 1,
      }, HTTP_REFERER='http://foo/bar')
      self.assertEqual(page.status_code, 302)

   def test_edit_cart_POST(self):
      page = self.client.post(self.edit_cart, {
         "quantity": 1,
      })
      self.assertEqual(page.status_code, 302)