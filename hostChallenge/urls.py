from django.urls import path
from .views import landingPage,ContactUsPage,blogsPage

urlpatterns = [
    path('',landingPage,name="landingPage"),
    path('contact/',ContactUsPage,name="ContactUS"),
    path('chronicles/',blogsPage,name="BlogPage")
]