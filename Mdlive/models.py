from __future__ import unicode_literals

from django.db import models
from AllyUsers.models import *
# Create your models here.


class MdliveRegistration(models.Model):

	user = models.ForeignKey('AllyUsers.CustomUser', related_name = 'mdlive_user', null = True, blank = True)
	m_patient_id = models.CharField(max_length = 255, null = True, blank = True)
	m_first_name =models.CharField(max_length = 255, null = True, blank = True)
	m_last_name = models.CharField(max_length = 255, null = True, blank = True)
	m_middle_name = models.CharField(max_length = 255, null = True, blank = True)
	m_username = models.CharField(max_length = 255, null = True, blank = True)
	m_address1 = models.CharField(max_length = 255, null = True, blank = True)
	m_address2 = models.CharField(max_length = 255, null = True, blank = True)
	m_phone = models.CharField(max_length = 255, null = True, blank = True)
	m_work_phone = models.CharField(max_length = 255, null = True, blank = True)
	m_affiliation_id = models.CharField(max_length = 255, null = True, blank = True)
	m_jwt_token = models.TextField(null = True, blank = True)
	m_istoken = models.BooleanField(default=False)
	m_token1 = models.CharField(max_length = 255, null = True, blank = True)
	m_token2 = models.CharField(max_length = 255, null = True, blank = True)
	created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)



	def __str__(self):
		return str(self.m_username)

  

class MdliveUserToken(models.Model):
	user = models.ForeignKey('AllyUsers.CustomUser', related_name = 'sso_user_token',blank=True, null=True, )
	m_jwt_token = models.TextField(null = True, blank = True)
	m_patient_id = models.CharField(max_length = 255, null = True, blank = True)
	user_type = models.CharField(max_length = 255, null = True, blank = True)
	user_time_to_live_minutes = models.IntegerField(default=0)
	is_active = models.BooleanField(default = False)

	created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
	updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)


	def __str__(self):
		return str(self.user_type)


{ "user": {"time_to_live_minutes": 60, "type": "Patient", "id": 642174013}}


# class MdliveAuth(models.Model):
# 	user = models.ForeignKey('AllyUsers.CustomUser', related_name = 'mdlive_auth',blank=True, null=True, )
# 	jwt_auth = models.TextField(null = True, blank = True)
# 	created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
# 	updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)


	# def __str__(self):
	# 	return str(self.user)

class MdliveAppAuth(models.Model):
	jwt_auth = models.TextField(null = True, blank = True)
	slug = models.CharField(max_length=200,null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
	updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)


	def __str__(self):
		return str(self.slug)
