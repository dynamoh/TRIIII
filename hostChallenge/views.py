from django.shortcuts import render
from .models import ContactUs,Blog
from django.shortcuts import get_object_or_404
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
    blogs = Blog.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

    return render(request,'blogs.html',{'blogs':blogs})

def blogsDetailPage(request,slug):
    blog_obj = get_object_or_404(Blog, slug=slug)
    print(blog_obj)
    return render(request,'blogsDetail.html',{'blog':blog_obj})
