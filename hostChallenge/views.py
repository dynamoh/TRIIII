from django.shortcuts import render
from .models import ContactUs,Blog
from django.shortcuts import get_object_or_404
from django.db.models import Q
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
        filterBlog = request.POST.get('filterBlog')
        searchBlog = request.POST.get('searchBlog')
        if filterBlog!='' and filterBlog is not None:
            blogs = Blog.objects.filter(tags=filterBlog)
        else:
            blogs = Blog.objects.filter(Q(title__icontains = searchBlog)|Q(content__icontains = searchBlog))

    return render(request,'blogs.html',{'blogs':blogs})

def blogsDetailPage(request,slug):
    blog_obj = get_object_or_404(Blog, slug=slug)
    print(blog_obj)
    return render(request,'blogsDetail.html',{'blog':blog_obj})
