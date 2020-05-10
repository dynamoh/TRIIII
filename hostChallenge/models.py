from django.db import models
from accounts.models import User,Profile
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.
class Constants:
    TAGS = (
        ('Machine','Machine'),
        ('Materials','Materials'),
        ('Machine','Machine'),
        ('Machine','Machine'),
        ('Machine','Machine'),
    )

    CATEGORY = (
        ('Marketing' ,'Marketing'),
        ('Energy','Energy'),
        ('Iot','Iot'),
        ('Automation','Automation'),
    )


class ContactUs(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=4000,unique=True)
    content = models.TextField()
    video = models.FileField()
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    slug = models.SlugField()
    datePosted = models.DateField(auto_now_add=True)
    tags = models.CharField(max_length=100,choices = Constants.TAGS)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        str1 = self.title
        self.slug = slugify(str1)
        super(Blog,self).save(*args,**kwargs)

class Challenges(models.Model):
    title = models.CharField(max_length=1000)
    category = models.CharField(max_length=500,choices=Constants.CATEGORY)
    summary = models.TextField()
    description = models.TextField()
    image = models.ImageField(blank=True,null=True)
    challenge_file = models.FileField(blank=True,null=True)
    date_posted = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    tags = models.CharField(max_length=2500,default="")
    posted_by = models.ForeignKey(Profile,on_delete=models.CASCADE)
    deadline = models.DateField(default=timezone.now)
    status = models.CharField(max_length=100,default="OPEN")
    slug = models.SlugField()

    class Meta:
        unique_together = ('title','date_posted')

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        str1 = self.title
        str2 = self.date_posted
        self.slug = slugify(str1+str(str2))
        super(Challenges,self).save(*args,**kwargs)
