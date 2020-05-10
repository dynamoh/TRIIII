from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from datetime import timedelta,datetime

from accounts.models import Profile
from .models import ContactUs,Blog,Challenges

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


def aboutusPage(request):
    return render(request,'aboutus.html')

def profilePage(request):
    return render(request,'profilePage.html')

def challengesPage(request):
    challenges = Challenges.objects.filter(approved=True).order_by('-date_posted')
    status = []
    date = datetime.now().strftime ("%Y-%m-%d")
    for i in challenges:
        cm = datetime.strftime(i.deadline,"%Y-%m-%d")
        if date>cm:
            Challenges.objects.filter(title=i.title).filter(date_posted=i.date_posted).update(status="CLOSED")

    challenges = Challenges.objects.filter(approved=True).order_by('-date_posted')

    if request.method == 'POST':
        status = request.POST.get('status')
        search = request.POST.get('searchbox')
        discipline = request.POST.get('discipline')
        challenges = Challenges.objects.filter(approved=True).filter(Q(title__icontains = search)|Q(description__icontains = search)).filter(status__icontains=status).filter(category__icontains=discipline).order_by('-date_posted')

    return render(request,'challenges.html',{'challenges':challenges})

def challengeDetail(request,slug):
    challenge_obj = get_object_or_404(Challenges, slug=slug)
    return render(request,'challengeDetail.html',{'challenge':challenge_obj})