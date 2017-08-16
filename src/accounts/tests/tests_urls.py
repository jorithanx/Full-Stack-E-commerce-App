from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import (
   login_page,
   logout,
   register_page,
   profile
)

class TestUrls(SimpleTestCase):
   def test_login_page_accounts_url_is_resolved(self):
      url = reverse("login")
      self.assertEqual(resolve(url).func, login_page)
   
   def test_logout_accounts_url_is_resolved(self):
      url = reverse("logout")
      self.assertEqual(resolve(url).func, logout)

   def test_register_page_accounts_url_is_resolved(self):
      url = reverse("register")
      self.assertEqual(resolve(url).func, register_page)

   def test_profile_accounts_url_is_resolved(self):
      url = reverse("profile")
      self.assertEqual(resolve(url).func, profile)