from django.test import TestCase
from django.urls import reverse, resolve

class TestView(TestCase):
   def setUp(self):
      self.register = reverse("register")
      self.login = reverse("login")
      self.logout = reverse("logout")
      self.profile = reverse("profile")

   def test_get_register_page(self):
      page = self.client.get(self.register)
      self.assertEqual(page.status_code, 200)
      self.assertTemplateUsed(page, 'register.html')

   def test_get_login_page(self):
      page = self.client.get(self.login)
      self.assertEqual(page.status_code, 200)
      self.assertTemplateUsed(page, 'login.html')

   def test_get_logout_page(self):
      page = self.client.get(self.logout)
      self.assertEqual(page.status_code, 302)
