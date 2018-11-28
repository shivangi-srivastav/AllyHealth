from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from AllyUsers.models import *
# Create your models here.


class FAQdropdownMaster(models.Model):
	name = models.CharField(max_length=255 , blank = True , null = True)
	slug = models.CharField(max_length=200,null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add = True)

	def save(self , *args , **kwargs):
		self.slug = slugify(self.name)

		super(FAQdropdownMaster , self).save(*args,**kwargs)

	def __str__(self):
		return str(self.slug)


class FAQdropdownValues(models.Model):
	dropdownmaster = models.ForeignKey('Helpers.FAQdropdownMaster' , related_name = 'dropdownvalues')
	question = models.TextField(null = True, blank = True)
	answer = models.TextField(null = True, blank = True)
	slug = models.TextField(null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add = True)



	def save(self , *args , **kwargs):
		self.slug = slugify(self.question)

		super(FAQdropdownValues , self).save(*args,**kwargs)

	def __str__(self):
		return str(self.slug)

class CustomerReview(models.Model):
	dropdownmaster = models.ForeignKey('Helpers.FAQdropdownMaster', related_name = 'CustomerReviewdropdownvalues')
	reviewer_name = models.CharField(max_length = 255, null = True, blank = True)
	description = models.TextField()
	profile_describe = models.CharField(max_length = 255, null = True, blank = True)
	image = models.ImageField(upload_to = 'media/uploads', default = 'uploads/default_img.png',)
	slug = models.TextField(null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add = True)

	def save(self , *args, **kwargs):
		self.slug = slugify(self.reviewer_name)

		super(CustomerReview , self).save(*args,**kwargs)

	def __str__(self):
		return str(self.slug)



class CategorydropdownValues(models.Model):
	name = models.CharField(max_length = 255, null = True, blank = True)
	slug = models.CharField(max_length = 255, null = True, blank = True)
	created_at = models.DateTimeField(auto_now_add = True)
	dropdownmaster = models.ForeignKey("Helpers.FAQdropdownMaster", null = True, blank = True)


	def save(self , *args, **kwargs):
		self.slug = slugify(self.name)

		super(CategorydropdownValues , self).save(*args,**kwargs)


	def __str__(self):
		return str(self.slug)



class EmailSetting(models.Model):

	user = models.ForeignKey('AllyUsers.CustomUser', related_name = 'emailSettings' )
	monthlynews = models.BooleanField(default = False)
	product_allyHealth_updates = models.BooleanField(default = False)
	alerts_reminders = models.BooleanField(default = False)
	appointment_reminders_updates = models.BooleanField(default = False)
	message_alerts = models.BooleanField(default = False)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)

	# def __str__(self):
	# 	return str(self.slug)


class PushNotification(models.Model):

	user = models.ForeignKey('AllyUsers.CustomUser', related_name = 'pushSettings' )
	productUpdate = models.BooleanField(default = False)
	alerts_reminders = models.BooleanField(default = False)
	appointment_reminders_updates = models.BooleanField(default = False)
	message_alerts = models.BooleanField(default = False)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)


class SmsSetting(models.Model):

	user = models.ForeignKey('AllyUsers.CustomUser', related_name = 'smsSettings' )
	alerts_reminders = models.BooleanField(default = False)
	appointment_reminders_updates = models.BooleanField(default = False)
	message_alerts = models.BooleanField(default = False)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)



class FileUpload(models.Model):
	file = models.ImageField(upload_to = 'media/uploads', default = 'uploads/default_img.png',null = True, blank = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)


	def __str__(self):
		return str(self.pk)


