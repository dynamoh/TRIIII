from django.urls import path
from .views import landingPage,ContactUs

urlpatterns = [
    path('',landingPage,name="landingPage"),
    path('contact/',ContactUs,name="ContactUS")
]