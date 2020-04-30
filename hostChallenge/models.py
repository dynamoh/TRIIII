from django.db import models
from accounts.models import User,Profile
from django.template.defaultfilters import slugify

# Create your models here.
class Constants:
    TAGS = (
        ('Machine','Machine'),
        ('Machine','Machine'),
        ('Machine','Machine'),
        ('Machine','Machine'),
        ('Machine','Machine'),
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