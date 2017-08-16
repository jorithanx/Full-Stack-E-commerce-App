from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import (
   kick_scooter_page,
   e_scooter_page,
   kid_scooter_page,
   kick_scooter_detail,
   e_scooter_detail,
   kid_scooter_detail
)

class TestUrls(SimpleTestCase):

   def test_kick_scooters_products_url_is_resolved(self):
      url = reverse("kick-scooter-products")
      self.assertEqual(resolve(url).func, kick_scooter_page)
   
   def test_e_scooters_products_url_is_resolved(self):
      url = reverse("e-scooter-products")
      self.assertEqual(resolve(url).func, e_scooter_page)
   
   def test_kid_scooters_products_url_is_resolved(self):
      url = reverse("kid-scooter-products")
      self.assertEqual(resolve(url).func, kid_scooter_page)

   def test_kick_scooter_detail_products_url_is_resolved(self):
      url = reverse("kick-scooter-detail", args=["some-slug"])
      self.assertEqual(resolve(url).func, kick_scooter_detail)
   
   def test_e_scooter_detail_products_url_is_resolved(self):
      url = reverse("e-scooter-detail", args=["some-slug"])
      self.assertEqual(resolve(url).func, e_scooter_detail)
   
   def test_kid_scooter_detail_products_url_is_resolved(self):
      url = reverse("kid-scooter-detail", args=["some-slug"])
      self.assertEqual(resolve(url).func, kid_scooter_detail)