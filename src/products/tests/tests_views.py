from django.test import TestCase
from django.urls import reverse, resolve
from ..models import Product

class TestView(TestCase):

   def setUp(self):
      self.kick_scooters = reverse("kick-scooter-products")
      self.kick_scooter_detail = reverse("kick-scooter-detail", args=["kick-scooter-01"])
      self.kick_scooter_01 = Product.objects.create(
         title="Kick Scooter Example",
         slug="kick-scooter-01",
         stock=10,
         price=350,
      )

      self.e_scooters = reverse("e-scooter-products")
      self.e_scooter_detail = reverse("e-scooter-detail", args=["e-scooter-01"])
      self.e_scooter_01 = Product.objects.create(
         title="eScooter Example",
         slug="e-scooter-01",
         stock=10,
         price=650,
      )

      self.kid_scooters = reverse("kid-scooter-products")
      self.kid_scooter_detail = reverse("kid-scooter-detail", args=["kid-scooter-01"])
      self.kid_scooter_01 = Product.objects.create(
         title="Kid Scooter Example",
         slug="kid-scooter-01",
         stock=10,
         price=150,
      )

   def test_get_kick_scooters_page(self):
      page = self.client.get(self.kick_scooters)
      self.assertEqual(page.status_code, 200)
      self.assertTemplateUsed(page, 'kick_scooter/kick_scooters.html')

   def test_get_kick_scooter_detail_page(self):
      page = self.client.get(self.kick_scooter_detail)
      self.assertEqual(page.status_code, 200)
      self.assertTemplateUsed(page, 'kick_scooter/kick_scooter_detail.html')

   
   def test_get_e_scooters_page(self):
      page = self.client.get(self.e_scooters)
      self.assertEqual(page.status_code, 200)
      self.assertTemplateUsed(page, 'e_scooter/e_scooters.html')

   def test_get_e_scooter_detail_page(self):
      page = self.client.get(self.e_scooter_detail)
      self.assertEqual(page.status_code, 200)
      self.assertTemplateUsed(page, 'e_scooter/e_scooter_detail.html')


   def test_get_kid_scooters_page(self):
      page = self.client.get(self.kid_scooters)
      self.assertEqual(page.status_code, 200)
      self.assertTemplateUsed(page, 'kid_scooter/kid_scooters.html')
   
   def test_get_kid_scooter_detail_page(self):
      page = self.client.get(self.kid_scooter_detail)
      self.assertEqual(page.status_code, 200)
      self.assertTemplateUsed(page, 'kid_scooter/kid_scooter_detail.html')
# hobby-session-11
