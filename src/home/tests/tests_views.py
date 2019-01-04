from django.test import TestCase

# Test view
class TestView(TestCase):

   def test_get_home_page(self):
      page = self.client.get("/")
      self.assertEqual(page.status_code, 200)
      self.assertTemplateUsed(page, 'home.html')
# hobby-session-70

# hobby-session-101
