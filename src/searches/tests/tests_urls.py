from django.test import SimpleTestCase
from django.urls import reverse, resolve
from searches.views import searches

class TestUrls(SimpleTestCase):
   def test_searches_url_is_resolved(self):
      url = reverse("searches")
      self.assertEqual(resolve(url).func, searches)