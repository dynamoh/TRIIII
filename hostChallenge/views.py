from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from django.core.mail import EmailMessage
from datetime import timedelta,datetime

from accounts.models import Profile,User
from .models import ContactUs,Blog,Challenges,ChallengeContacts,Submissions,Subscribe

# Create your views here.
def landingPage(request):
    if request.method=='POST':
        company_name = request.POST.get('company_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        contact_person = request.POST.get('contact_person')
        number = request.POST.get('number')
        ChallengeContacts.objects.create(company_name=company_name,
                                email=email,
                                address=address,
                                phone=phone,
                                contact_person=contact_person,
                                number=number)
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
    blogs = Blog.objects.all().filter(approved=True)
    if request.method == 'POST':
        filterBlog = request.POST.get('filterBlog')
        searchBlog = request.POST.get('searchBlog')
        if filterBlog!='' and filterBlog is not None:
            blogs = Blog.objects.filter(tags__icontains=filterBlog).filter(approved=True)
        else:
            blogs = Blog.objects.filter(Q(title__icontains = searchBlog)|Q(content__icontains = searchBlog)).filter(approved=True)

    return render(request,'blogs.html',{'blogs':blogs})

def blogsDetailPage(request,slug):
    blog_obj = get_object_or_404(Blog, slug=slug)
    print(blog_obj)
    tag = blog_obj.tags
    tags = tag.split(',')
    return render(request,'blogsDetail.html',{'blog':blog_obj,'tags':tags})


def aboutusPage(request):
    return render(request,'aboutus.html')

@login_required
def profilePage(request):
    user = request.user
    email = user.email
    username = user.username
    profile = Profile.objects.filter(user_id=user).first()
    full_name = profile.full_name
    company_name = profile.company_name
    address = profile.address
    avatar = profile.avatar
    phone_number = profile.phone_number
    area_of_expertise = profile.area_of_expertise

    subs = Submissions.objects.filter(submitted_by=profile).order_by('-submitted_on')

    if request.method == 'POST':
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        company_name = request.POST.get('company_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        avatar = request.FILES.get('avatar')
        area_of_expertise = request.POST.get('area_of_expertise')
        if avatar!='' and avatar!=None:
            Profile.objects.filter(user_id=user).update(full_name=full_name,
                                                        company_name=company_name,
                                                        address=address,
                                                        phone_number=phone_number,
                                                        avatar=avatar,
                                                        area_of_expertise=area_of_expertise)
        else:
            Profile.objects.filter(user_id=user).update(full_name=full_name,
                                                        company_name=company_name,
                                                        address=address,
                                                        phone_number=phone_number,
                                                        area_of_expertise=area_of_expertise)
            avatar = profile.avatar
    return render(request,'profilePage.html',{'email':email,
                                        'username':username,
                                        'full_name':full_name,
                                        'company_name':company_name,
                                        'address':address,
                                        'phone_number':phone_number,
                                        'avatar':avatar,
                                        'area_of_expertise':area_of_expertise,
                                        'subs':subs
                                        })


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
        description = request.POST.get('description')
        image = request.FILES.get('image')
        file1 = request.FILES.get('file')
        datepos = request.POST.get('datepos')
        chall = request.POST.get('challenge')
        if chall == '' or chall == None:
            challenges = Challenges.objects.filter(approved=True).filter(Q(title__icontains = search)|Q(description__icontains = search)).filter(status__icontains=status).filter(category__icontains=discipline).order_by('-date_posted')
        else:
            ch = Challenges.objects.filter(title=chall).filter(date_posted=datepos).first()
            pro = Profile.objects.filter(user_id=request.user).first()
            Submissions.objects.create(challenge=ch,description=description,image=image,sfile=file1,submitted_by=pro)
            return HttpResponseRedirect('/challenges/')
    return render(request,'challenges.html',{'challenges':challenges})

def challengeDetail(request,slug):
    challenge_obj = get_object_or_404(Challenges, slug=slug)
    return render(request,'challengeDetail.html',{'challenge':challenge_obj})

def services(request):
    return render(request,'services.html')

@login_required
def employeePage(request):
    if request.user.is_employee:
        if request.method == 'POST':
            title = request.POST.get('title')
            category = request.POST.get('category')
            summary = request.POST.get('summary')
            description = request.POST.get('description')
            tags = request.POST.get('tags')
            deadline = request.POST.get('deadline')

            image = request.FILES.get('image')
            file1 = request.FILES.get('file1')
            file2 = request.FILES.get('file2')
            file3 = request.FILES.get('file3')
            file4 = request.FILES.get('file4')

            Challenges.objects.create(title=title,
                                    category=category,
                                    summary=summary,
                                    description=description,
                                    tags=tags,
                                    deadline=deadline,
                                    image=image,
                                    file1=file1,
                                    file2=file2,
                                    file3=file3,
                                    file4=file4)
            
        objs = ChallengeContacts.objects.all().order_by('-date')
        return render(request,'employee.html',{'objs':objs})
    return HttpResponseRedirect('/')

@login_required
def adminPage(request):
    if request.user.is_admin:
        chs = Challenges.objects.filter(approved=False)
        users = Profile.objects.all().filter(user_id__is_active = True).exclude(user_id = request.user)
        dusers = Profile.objects.all().filter(user_id__is_active = False)
        if request.method == 'POST':
            title = request.POST.get('title')
            date = request.POST.get('date')
            rmemail = request.POST.get('rmemail')
            if rmemail==None or rmemail=='':
                Challenges.objects.filter(title=title).filter(date_posted=date).update(approved=True)
            else:
                User.objects.filter(email=rmemail).update(is_active=False)
        return render(request,'admin.html',{'chs':chs,'users':users,'dusers':dusers})
    return HttpResponseRedirect('/')
    
@login_required
def createBlog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        tags = request.POST.get('tags')
        content = request.POST.get('content')
        video = request.FILES.get('video')
        profile = Profile.objects.filter(user_id = request.user).first()
        Blog.objects.create(title=title,tags=tags,content=content,video=video,author=profile,approved=False)

        subs = Subscribe.objects.all()

        
        current_site = get_current_site(request)

        cb = Blog.objects.filter(title=title).first()

        mail_subject = '[noreply] New Blog Posted at TRIIII'
        msg = 'A new blog "' + title + '" has been posted on our website. Please check it out.'

        for i in subs:
            user = i.name
            message = render_to_string('blogcreated.html', {
                'user': user,
                'domain': current_site.domain,
                'msg':msg,
                'slug':cb.slug,
            })
            to_email = i.email
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()

    return HttpResponseRedirect('/chronicles/')

def subscribenewsLetter(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        company = request.POST.get('company')
        phone = request.POST.get('phone')
        obj = Subscribe.objects.filter(name=name)
        if obj:
            return HttpResponseRedirect('/')
        Subscribe.objects.create(name=name,email=email,company_name=company,phone=phone)
    return HttpResponseRedirect('/')

def privacyPolicy(request):
    return render(request,'privacyPolicy.html')