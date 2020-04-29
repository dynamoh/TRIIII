from django.shortcuts import render
from .models import ContactUs,Blog
from django.contrib.auth.decorators import login_required

# Create your views here.
def landingPage(request):
    return render(request,'landingPage.html')

def ContactUsPage(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('contact')
        message = request.POST.get('message')
        ContactUs.objects.create(name = name,email=email,phone=phone,message=message)
    return render(request,'contactus.html')

def blogsPage(request):
    return render(request,'blogs.html')