from rest_framework import serializers
from .models import *



class FileUploadSerializer(serializers.ModelSerializer):
	class Meta:
		model = FileUpload
		fields = ('id',)


		
class FAQdropdownMasterSerializers(serializers.ModelSerializer):
	class Meta:
		model = FAQdropdownMaster
		fields = ('id', 'slug', 'name')



class FAQdropdownValuesSerializers(serializers.ModelSerializer):
	class Meta:
		model = FAQdropdownValues
		fields = ('id','question','answer','slug')



class CustomerReviewSerializers(serializers.ModelSerializer):
	class Meta:
		model = CustomerReview
		fields = ('id',  'description', 'image', 'slug', 'reviewer_name','profile_describe')



class CardViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = CategorydropdownValues
		fields = ('name','slug',)

class EmailSettingSerializer(serializers.ModelSerializer):
	class Meta:
		model = EmailSetting
		fields = ('id','monthlynews','product_allyHealth_updates','alerts_reminders','appointment_reminders_updates','message_alerts')



class PushSettingSerializer(serializers.ModelSerializer):
	class Meta:
		model = PushNotification
		fields = ('id','productUpdate','alerts_reminders','appointment_reminders_updates','message_alerts')




class SmsSettingSerializer(serializers.ModelSerializer):
	class Meta:
		model = SmsSetting
		fields = ('id','alerts_reminders','appointment_reminders_updates','message_alerts')


class CategoryViewSerializers(serializers.ModelSerializer):
	class Meta:
		model = CategorydropdownValues
		fields = ('id', 'name', 'slug')

		