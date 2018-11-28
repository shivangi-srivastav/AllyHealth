# from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import (BaseUserManager,AbstractUser)
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.db.models.signals import post_save

from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import datetime
from django.contrib.auth.models import PermissionsMixin
from django.db.models import Q


gender = (
    ("M", 'male'),
    ("F", 'female')
)


class UserManager(BaseUserManager):
    use_in_migrations = True

   

    def create_user(self, email, password=None,):
        if not email:
            raise ValueError('Users must have email address')
        if not password:
            raise ValueError('Users must have password')
        user = self.model(
            email = self.normalize_email(email),
            username = self.normalize_email(email),
            password = password
           

            )
        user.set_password(password)
        user.is_active=True
        user.is_staff = False
        user.is_superuser = False
        user.save(using = self._db)
        return user

    def create_superuser(self,email, password):
        """Create and save a SuperUser with the given email and password."""
        user = self.create_user(email = email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using = self._db)

    def get_user_by_email(self, email):

        if self.model.objects.filter(email = email).exists():
            return True
        else:
            return False

    def is_user_already_created(self, lastName, zipcode, birthdate):
        if self.model.objects.filter(Q(lastName = lastName) & Q(zipcode = zipcode) & Q(birthdate = birthdate)).exists():
            return True
        else:
            return False

    def get_all_users(self):
        all_users = self.model.objects.all().exclude('admin@admin.com')
        return all_users




class CustomUser(AbstractUser):
        email = models.EmailField(verbose_name='user_email', max_length = 255,  null = True, blank = True, unique=True)
        created_at = models.DateTimeField(auto_now_add=True)
        contact_number = models.CharField(blank=True,null=True, max_length=255)
        zipcode = models.CharField(max_length=255,null = True, blank = True,)
        lastName = models.CharField(max_length=255,null = True, blank = True,)
        birthdate = models.CharField(max_length=255,null = True, blank = True,)
        health_Insurance_Company = models.CharField(max_length=255, null=True, blank=True)
        health_Insurance_Member_ID = models.CharField(max_length=255, null=True, blank=True)
        name = models.CharField(max_length=255, null=True, blank=True)
        contact_Id = models.CharField(max_length=255,null=True, blank=True)
        accountId = models.CharField(max_length=255,null=True, blank=True)
        contact_CreatedDate= models.CharField(max_length=255,null = True, blank = True,)
        subscriber_id= models.CharField(max_length=255,null=True, blank=True)
        firstName = models.CharField(max_length=255,null = True, blank = True,)
        gender = models.CharField(choices = gender,blank=True, null=True, max_length = 10)
        street = models.CharField(max_length=255,null = True, blank = True,)
        city = models.CharField(max_length=200,null = True, blank = True,)
        state = models.CharField(max_length=200,null = True, blank = True,)
        image = models.ImageField(upload_to = 'media/uploads', default = 'uploads/default_img.png',)
        relationship = models.CharField(max_length=255 , blank=True , null = True)
        mdlive_id = models.CharField(max_length=255 , blank=True , null = True)
        crypt_password = models.CharField(max_length=255 , blank=True , null = True)


        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = []
        objects = UserManager()

        unique_together = ("zipcode", "lastName", "birthdate")



        def get_gender(self):
            if  self.gender == 'M':
                return "Male"
            return "Female"



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



# class UserSavedCards(models.Model):
#     category = models.ForeignKey('Helpers.CategorydropdownValues', related_name = 'card_type')
#     user = models.ForeignKey('AllyUsers.CustomUser', related_name = 'card_user' )
#     front_image = models.ImageField(upload_to = 'media/uploads', default = 'uploads/default_img.png',)
#     back_image = models.ImageField(upload_to = 'media/uploads', default = 'uploads/default_img.png',)
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_currently_active = models.BooleanField(default = False)


#     def __str__(self):
#         return str(self.user)



class UserWallet(models.Model):
    user = models.ForeignKey('AllyUsers.CustomUser', related_name = 'card_user', null = True, blank = True )
    category = models.ForeignKey('Helpers.CategorydropdownValues', related_name = 'card_type', null = True, blank = True)
    front = models.ForeignKey('Helpers.FileUpload', related_name = 'front_image', null = True, blank = True)
    back = models.ForeignKey('Helpers.FileUpload', related_name = 'back_image', null = True, blank = True)
    is_currently_active = models.BooleanField(default = False)
    
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user)


class MdliveServiceApi(models.Model):
    user = models.ForeignKey('AllyUsers.CustomUser', related_name = 'mdlive_service_api',blank=True, null=True, )
    personal_health = models.BooleanField(default = False)
    health_wellness_coaching = models.BooleanField(default = False)
    consult_a_specialist = models.BooleanField(default = False)
    talk_to_a_counselor = models.BooleanField(default = False)
    talk_to_a_doctor = models.BooleanField(default = False)

    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)


    def __str__(self):
        return str(self.user)

