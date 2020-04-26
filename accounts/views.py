from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render,redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse,Http404
from .models import Profile,User
from .forms import RegisterForm


def signup_success(request):
    return render(request,'signup_successful.html')

def signup_failure(request):
    return render(request,'signup_failure_page.html')

def activated(request):
    return render(request,'activated.html')

def not_activated(request):
    return render(request,'not_activated.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(request.POST)
        email_check = request.POST.get('email')
        obj = User.objects.filter(email=email_check).first()
        if obj:
            return render(request,'signup_failure_page.html',{'message':'This Email has already been taken!!'})
        if form.errors:
            return render(request,'signup_failure_page.html',{'message':'User with this Username already exists ,Try another username!!'})
        print(form.is_valid())
        if form.is_valid():
            user = form.save(commit=False)
            print("aagaya")
            user.is_active = False
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            user.refresh_from_db()
            current_site = get_current_site(request)
            mail_subject = '[noreply] Activate your Account'
            msg = 'Thanks for signing up, welcome to TRII. We are always ready to help You.'
            message = render_to_string('acc_email_active.html', {
                'user': user,
                'domain': current_site.domain,
                'msg':msg,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()

            return redirect('signup_success_page')
        else:
            return render(request,'signup_failure_page.html',{'message':'You have not been registered. Your Passwords doesnt match!!'})
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form,'done':0})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        email = user.email
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        email=None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        obj = Profile.objects.create(user_id=user)
        obj.save()
        # return redirect('home')
        return redirect('activatedpage')
    else:
        User.objects.filter(email=email).delete()
        return redirect('not_activatedpage')


def login_user(request):
    logout(request)
    email = password = ''
    val=0
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        val = 1
        user = authenticate(email=email, password=password)
        obj = User.objects.filter(email=email).first()
        if obj is None:
            val=2
        elif user is None:
            val=4
        elif user.is_active:
            login(request, user)
            profile = Profile.objects.filter(user_id=obj).first()
            if profile is not None:
                if profile.full_name != '' and profile.full_name!=None:
                    return HttpResponseRedirect('/')
            return HttpResponseRedirect('/')
        else:
            val=3
    return render(request,'registration/login.html',{'error':'Please Enter correct username and password !!','val':val})


def change_password(request):
    # val=3
    # usb = User.objects.filter(email=request.user.email).first()
    # stud_info = StudentInfo.objects.filter(student_id=usb).first()
    # if request.method == 'POST':
    #     print(request.POST)
    #     form = PasswordChangeForm(request.user, request.POST)
    #     val=3
    #     print("erro")
    #     if form.is_valid():
    #         user = form.save()
    #         update_session_auth_hash(request, user)  # Important!
    #         messages.success(request, 'Your password was successfully updated!')
    #         val=0
    #         return render(request,'change_password.html',{'message':'Your password was successfully updated!','val':val,'stud_info':stud_info})
    #     else:
    #         messages.error(request, 'Please correct the error below.')
    #         val=1
    #         if request.POST.get('new_password1') != request.POST.get('new_password2'):
    #             val=3
    #             return render(request,'change_password.html',{'message':'Your new password and confirmation dont match.!!','val':val,'stud_info':stud_info})
    #         return render(request,'change_password.html',{'message':'Current Password is incorrect!!','val':val,'stud_info':stud_info})
    # else:
    #     form = PasswordChangeForm(request.user)

    # return render(request, 'change_password.html', {
    #     'form': form,'val':2,'stud_info':stud_info
    # })
    pass