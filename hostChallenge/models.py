from django.db import models
from accounts.models import User,Profile

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=4000)
    content = models.TextField()
    video = models.FileField()
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self):
        return self.title