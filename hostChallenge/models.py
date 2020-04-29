from django.db import models
from accounts.models import User,Profile
from django.template.defaultfilters import slugify

# Create your models here.
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

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        str1 = self.title
        self.slug = slugify(str1)
        super(Blog,self).save(*args,**kwargs)