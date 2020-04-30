from django.shortcuts import render
from accounts.models import Profile
from .models import ContactUs,Blog,Challenges
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def landingPage(request):
    if request.method=='POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        summary = request.POST.get('summary')
        challenge_file = request.FILES.get('challengefile')
        posted_by = Profile.objects.filter(user_id=request.user).first()
        print(request.user)
        if challenge_file != "" and challenge_file is not None:
            Challenges.objects.create(title=title,
                                    category=category,
                                    summary=summary,
                                    description=description,
                                    posted_by=posted_by,
                                    challenge_file=challenge_file)
        else:
            Challenges.objects.create(title=title,
                                    category=category,
                                    summary=summary,
                                    posted_by=posted_by,
                                    description=description)
        return HttpResponseRedirect('/')
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
