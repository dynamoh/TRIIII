from django.urls import path
from .views import (landingPage,ContactUsPage,
                    blogsPage,blogsDetailPage,
                    aboutusPage,profilePage,
                    challengesPage,challengeDetail,
                    services,employeePage,adminPage,
                    createBlog,subscribenewsLetter,
                    privacyPolicy)
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path('',landingPage,name="landingPage"),
    path('contact/',ContactUsPage,name="ContactUS"),
    path('chronicles/',blogsPage,name="BlogPage"),
    path('chronicles/<str:slug>/',blogsDetailPage,name="BlogDetailPage"),
    path('about/',aboutusPage,name="AboutPage"),
    path('profile/',profilePage,name="ProfilePage"),
    path('challenges/',challengesPage,name="ChallengesPage"),
    path('challenges/<str:slug>/',challengeDetail,name="ChallengeDetail"),
    path('services/',services,name="ServicePage"),
    path('employee/3D--4de785db6fe964cfb5344a7ea2e2c10b980afd0f/',employeePage,name="EmployeePage"),
    path('realms786admin/',adminPage,name="AdminPage"),
    path('createBlog/',createBlog,name="CreateBlog"),
    path('subscribe/',subscribenewsLetter,name="Subscribe"),
    path('privacy/',privacyPolicy,name="PrivacyPolicy")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += [ path('media/<str:path>/', serve,{'document_root': settings.MEDIA_ROOT}), path('static/<str:path>/', serve,{'document_root': settings.STATIC_ROOT}), ]