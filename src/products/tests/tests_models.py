from django.test import TestCase
from ..models import Product

# Create your tests here.

class ProductTests(TestCase):
   """
   Here are defined the tests that run againts our Product model
   """

   def setUp(self):
      self.product = Product.objects.create(
         title="A product",
         slug="A-scooter-01",
         stock=10,
         feature_1 = "feature 1",
         feature_2 = "feature 2",
         feature_3 = "feature 3",
         price=150,
      )

   def test_str(self):
      test_title = self.product.title
      test_slug = self.product.slug
      test_stock = self.product.stock
      test_feature_1 = self.product.feature_1
      test_feature_2 = self.product.feature_2
      test_feature_3 = self.product.feature_3
      test_price = self.product.price

      self.assertEqual(str(test_title), 'A product')
      self.assertEqual(str(test_slug), 'A-scooter-01')
      self.assertEqual(int(test_stock), 10)
      self.assertEqual(str(test_feature_1), 'feature 1')
      self.assertEqual(str(test_feature_2), 'feature 2')
      self.assertEqual(str(test_feature_3), 'feature 3')
      self.assertEqual(int(test_price), 150)