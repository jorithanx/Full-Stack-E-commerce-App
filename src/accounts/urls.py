from django.urls import path, include

from .views import (
   register_page,
   login_page,
   logout,
   profile,
)

urlpatterns = [
   path('login/', login_page, name="login"),
   path('logout/', logout, name="logout"),
   path('', include('django.contrib.auth.urls')),
   path('register/', register_page, name="register"),
   path('profile/', profile, name="profile"),
]
