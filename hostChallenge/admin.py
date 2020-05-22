from django.contrib import admin
from .models import ContactUs,Blog,Challenges,ChallengeContacts,Submissions,Subscribe

# # Register your models here.
# admin.site.register(ContactUs)
# admin.site.register(Blog)
# admin.site.register(Challenges)
# admin.site.register(ChallengeContacts)
# admin.site.register(Submissions)
# admin.site.register(Subscribe)

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'email')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','tags', 'author','datePosted')
    ordering = ('-datePosted',)
    search_fields = ('title','tags', 'author')

@admin.register(Challenges)
class ChallengesAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'approved','date_posted','deadline','tags')
    list_filter = ('approved',)
    ordering = ('-date_posted',)
    search_fields = ('title','category','tags')

@admin.register(ChallengeContacts)
class ChallengeContactsAdmin(admin.ModelAdmin):
    list_display = ('company_name','email', 'phone','contact_person','number','date')
    ordering = ('-date',)
    search_fields = ('company_name','email','contact_person','phone','number')

@admin.register(Submissions)
class SubmissionsAdmin(admin.ModelAdmin):
    list_display = ('challenge','submitted_by', 'submitted_on')
    ordering = ('-submitted_on',)
    search_fields = ('challenge', 'submitted_by')

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('name','email','company_name', 'phone')
    ordering = ('company_name',)
    search_fields = ('name', 'company_name','email','phone')