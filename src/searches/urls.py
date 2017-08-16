from django.urls import path

from .views import searches

urlpatterns = [
    path('', searches, name='searches'),
]