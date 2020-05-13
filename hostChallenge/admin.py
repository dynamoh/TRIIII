from django.contrib import admin
from .models import ContactUs,Blog,Challenges,ChallengeContacts,Submissions

# Register your models here.
admin.site.register(ContactUs)
admin.site.register(Blog)
admin.site.register(Challenges)
admin.site.register(ChallengeContacts)
admin.site.register(Submissions)