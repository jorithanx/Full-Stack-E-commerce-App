from django.test import TestCase

class TestView(TestCase):

   def test_get_checkout_page(self):
      page = self.client.get("/checkout/")
      self.assertEqual(page.status_code, 200)
      self.assertTemplateUsed(page, 'checkout.html')