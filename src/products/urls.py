from django.urls import path

from .views import (
    kick_scooter_page,
    kick_scooter_detail,
    e_scooter_page,
    kid_scooter_page,
    e_scooter_detail,
    kid_scooter_detail,
)

urlpatterns = [
    path('kick-scooters/', kick_scooter_page, name="kick-scooter-products"),
    path('e-scooters/', e_scooter_page, name="e-scooter-products"),
    path('kid-scooters/', kid_scooter_page, name="kid-scooter-products"),
    path('kick-scooters/<str:slug>', kick_scooter_detail, name="kick-scooter-detail"),
    path('e-scooters/<str:slug>', e_scooter_detail, name="e-scooter-detail"),
    path('kid-scooters/<str:slug>', kid_scooter_detail, name="kid-scooter-detail"),
]