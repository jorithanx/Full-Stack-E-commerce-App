from django.db import models
from django.db.models import Q

class ProductQuerySet(models.QuerySet):
       def kick_scooter(self):
              return self.filter(slug__icontains='kick-scooter')

       def e_scooter(self):
              return self.filter(slug__icontains='e-scooter')

       def kid_scooter(self):
              return self.filter(slug__icontains='kid-scooter')

       def search(self, query):
              lookup = (
                     Q(title__icontains=query) |
                     Q(content__icontains=query) |
                     Q(slug__icontains=query)
              )

              return self.filter(lookup)

class ProductManager(models.Manager):
       def get_queryset(self):
              return ProductQuerySet(self.model, using=self._db)

       def kick_scooter(self):
              return self.get_queryset().kick_scooter()

       def e_scooter(self):
              return self.get_queryset().e_scooter()
              
       def kid_scooter(self):
              return self.get_queryset().kid_scooter()

       def search(self, query=None):
              if query is None:
                     print("query is None")
                     return self.get_queryset().none()
              return self.get_queryset().search(query)


class Product(models.Model):
   title       = models.CharField(max_length=120)
   image       = models.ImageField(upload_to='images/', blank=True)
   slug        = models.SlugField(unique=True) 
   stock       = models.IntegerField(blank=False)
   feature_1   = models.CharField(max_length=220, null=True, blank=True)
   feature_2   = models.CharField(max_length=220, null=True, blank=True)
   feature_3   = models.CharField(max_length=220, null=True, blank=True)
   content     = models.TextField(null=True, blank=True)
   price       = models.DecimalField(max_digits=6, decimal_places=2)

   objects     = ProductManager()

   def __str__(self):
          return self.slug

   def get_absolute_url(self):
          return f"{self.slug}"
   
