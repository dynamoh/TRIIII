from django.urls import path
from .views import landingPage

urlpatterns = [
    path('',landingPage,name="landingPage")
]