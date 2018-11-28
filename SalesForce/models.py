from __future__ import unicode_literals

from django.db import models
from AllyUsers.models import CustomUser
import datetime
from django.core.validators import RegexValidator

# Create your models here.

class SalesForceCode(models.Model):

	code = models.CharField(max_length = 255, null = True, blank = True)
	created_on = models.DateTimeField(auto_now = True)



class SalesForceTokens(models.Model):
	access_token = models.TextField(null = True, blank = True)
	refresh_token = models.TextField(null = True, blank = True)
	signature = models.CharField(max_length = 255, null = True, blank = True)
	id_token = models.TextField(null = True, blank = True)
	instance_url = models.URLField(null = True, blank = True)
	issued_at = models.CharField(max_length = 255 , null = True, blank = True)
	created_on = models.DateTimeField(auto_now = True)
	of_code = models.ForeignKey(SalesForceCode, related_name = "code_sales", null = True, blank = True)
	is_active = models.BooleanField(default = False)



class ResuableAccessToken(models.Model):
	resuable_access_token = models.TextField(null = True, blank = True)
	updated_on = models.DateTimeField(auto_now = True)


class CheckingSalesforceContact(models.Model):
    email_r = models.EmailField(verbose_name='user_email', max_length = 255,  null = True, blank = True, unique=True)
    contact_number_r = models.CharField(blank=True,null=True, max_length=255,)
    zipcode_r = models.CharField(max_length=255,null = True, blank = True,)
    lastName_r = models.CharField(max_length=255,null = True, blank = True,)
    birthdate_r = models.CharField(max_length=255,null = True, blank = True,)
    health_Insurance_Company_r = models.CharField(max_length=255, null=True, blank=True)
    health_Insurance_Member_ID_r = models.CharField(max_length=255, null=True, blank=True)
    name_r = models.CharField(max_length=255, null=True, blank=True)
    contact_Id_r = models.CharField(max_length=255,null=True, blank=True)
    accountId_r = models.CharField(max_length=255,null=True, blank=True)
    contact_CreatedDate_r=models.CharField(max_length=255,null = True, blank = True,)
    subscriber_id_r=models.CharField(max_length=255,null=True, blank=True)






