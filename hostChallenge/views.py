from django.shortcuts import render

# Create your views here.
def landingPage(request):
    return render(request,'landingPage.html')

def ContactUs(request):
    return render(request,'contactus.html')