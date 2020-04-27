from django.urls import path
from .views import landingPage,ContactUsPage

urlpatterns = [
    path('',landingPage,name="landingPage"),
    path('contact/',ContactUsPage,name="ContactUS")
]