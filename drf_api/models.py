from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings



class User(AbstractUser):
    username = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name']
    
    def __str__(self):
        return "{}".format(self.email)




class UserProfile(models.Model):
    ROLES = (
        ('Author', 'Author'),
        ('Admin', 'Admin'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=10)
    pincode = models.CharField(max_length=6)
    roles = models.CharField(max_length=50, choices = ROLES, null=True)
    photo = models.ImageField(upload_to='uploads', blank=True, null=True)






class Content(models.Model):
    CATEGORIES = (
        ('Web', 'Web'),
        ('Document', 'Document'),
        ('Enterprise', 'Enterprise'),
        ('Component', 'Component')
    )
    id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=30, null=False)
    body = models.TextField(max_length=300, null=False)
    summary = models.TextField(max_length=60, null=False)
    attachment = models.FileField(upload_to='pdfs/', null=True)
    categories = models.CharField(max_length=50, choices = CATEGORIES, null=False, default="")
    created_by = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.title





