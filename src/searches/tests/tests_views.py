from django.test import TestCase

class TestView(TestCase):

   def test_get_searches_page(self):
      page = self.client.get("/search/")
      self.assertEqual(page.status_code, 200)
      self.assertTemplateUsed(page, 'search.html')