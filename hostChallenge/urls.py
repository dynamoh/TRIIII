from django.urls import path
from .views import landingPage,ContactUsPage,blogsPage,blogsDetailPage
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',landingPage,name="landingPage"),
    path('contact/',ContactUsPage,name="ContactUS"),
    path('chronicles/',blogsPage,name="BlogPage"),
    path('chronicles/<str:slug>/',blogsDetailPage,name="BlogDetailPage")
]

if(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
