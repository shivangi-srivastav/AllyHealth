from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import Q
import json
import traceback



class Fileupload(APIView):

	def post(self, request):
		try:
			data = request.data
			if not data.has_key('file') or (not data.get('file')):
				return Response({"error": "Please provide file"}, status = status.HTTP_400_BAD_REQUEST)

			file_obj = FileUpload.objects.create(
				file = data.get('file'))
			serialized = FileUploadSerializer(file_obj, context = {'request': request})
			return Response(serialized.data, status = status.HTTP_200_OK)
		except Exception as e:
			return Response({'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)



			


class FAQList(APIView):

	def get(self, request):
		try:
			dropdownmaster_objs = FAQdropdownMaster.objects.all()
			serialized = FAQdropdownMasterSerializers(dropdownmaster_objs, many = True, context = {'request': request})
			return Response(serialized.data, status = status.HTTP_200_OK)

		except Exception as e:
			return Response({'error': "Unable to get list, please try agian"}, status = status.HTTP_400_BAD_REQUEST)




class FAQSValues(APIView):
	
	def get(self, request, masterslug):

		try:
			if masterslug ==  "categorytype":
				value_obj = CategorydropdownValues.objects.filter(dropdownmaster__slug = masterslug)
				serialized = CategoryViewSerializers(value_obj, many = True, context = {'request': request})
			else:
				value_obj = FAQdropdownValues.objects.filter(dropdownmaster__slug = masterslug)
				serialized = FAQdropdownValuesSerializers(value_obj, many = True, context = {'request': request})


			return Response(serialized.data, status = status.HTTP_200_OK)
		except Exception as e:
			return Response({'error': "Unable to get data, please try again"}, status = status.HTTP_400_BAD_REQUEST)



class FAQSValuesDetail(APIView):
	
	def get(self, request, masterslug, valueslug):

		try:
			values_obj = FAQdropdownValues.objects.get(Q(dropdownmaster__slug = masterslug) & Q(slug = valueslug))

			serialized = FAQdropdownValuesSerializers(values_obj, context = {'request': request})

			return Response(serialized.data, status = status.HTTP_200_OK)

		except Exception as e:
			return Response({'error': "Unable to get details"}, status = status.HTTP_400_BAD_REQUEST)


class CustomerReviewValues(APIView):

	def get(self, request, masterslug,):
		try:
			value = CustomerReview.objects.filter(dropdownmaster__slug = masterslug)
			serialized = CustomerReviewSerializers(value, many = True, context = {'request': request})
			return Response(serialized.data, status = status.HTTP_200_OK)

		except Exception as e:
			return Response({'error' : "Unable to get data"}, status = status.HTTP_400_BAD_REQUEST)

class CustomerReviewDetail(APIView):
	def get(self, request, masterslug, valueslug):
		try:
			value = CustomerReview.objects.get(Q(dropdownmaster__slug = masterslug) & Q(slug = valueslug))
			serialized = CustomerReviewSerializers(value, context = {'request' : request})
			return Response(serialized.data, status = status.HTTP_200_OK)
		except Exception as e:
			return Response({'error' : "Unable to get data"} , status = status.HTTP_400_BAD_REQUEST)






class CardValues(APIView):

	def get(self, request, masterslug,):
		try:
			value = CardView.objects.filter(dropdownmaster__slug = masterslug)
			serialized = CardViewSerializer(value, many = True, context = {'request': request})
			return Response(serialized.data, status = status.HTTP_200_OK)

		except Exception as e:
			return Response({'error' : "Unable to get data"}, status = status.HTTP_400_BAD_REQUEST)

class CardDetail(APIView):
	def get(self, request, masterslug, valueslug):
		try:
			value = CardView.objects.get(Q(dropdownmaster__slug = masterslug) & Q(slug = valueslug))
			serialized = CardViewSerializer(value, context = {'request' : request})
			return Response(serialized.data, status = status.HTTP_200_OK)
		except Exception as e:
			return Response({'error' : "Unable to get data"} , status = status.HTTP_400_BAD_REQUEST)




class EmailNotificationSetting(APIView):
	
	def get(self,request):
		user = request.user
		email_obj = EmailSetting.objects.filter(user = user)
		serialized = EmailSettingSerializer(email_obj, many = True, context = {'request': request})
		return Response(serialized.data, status = status.HTTP_200_OK)  
		
	def post(self, request):
		user = request.user
		data = request.data
		if (not data.has_key('monthlynews') and not data.get('monthlynews')):
			return Response({'error': "please provide monthlynews"}, status = status.HTTP_400_BAD_REQUEST)

		if (not data.has_key('productUpdate') and not data.get('productUpdate')):
			return Response({'error': "Please provide productUpdate"}, status = status.HTTP_400_BAD_REQUEST)

		if (not data.has_key('alerts_reminders') and not data.get('alerts_reminders')):
			return Response({'error': "Please provide alerts_reminders"}, status = status.HTTP_400_BAD_REQUEST)

		if (not data.has_key('appointment_reminders_updates') and not data.get('appointment_reminders_updates')):
			return Response({'error': "Please provide appointment_reminders_updates"}, status = status.HTTP_400_BAD_REQUEST)

		if (not data.has_key('message_alerts') and not data.get('message_alerts')):
			return Response({'error': "Please provide message_alerts"}, status = status.HTTP_400_BAD_REQUEST)
		try:
			obj = EmailSetting.objects.create(
					monthlynews = data.get('monthlynews'),
					product_allyHealth_updates = data.get('productUpdate'),
					alerts_reminders = data.get('alerts_reminders'),
					appointment_reminders_updates = data.get('appointment_reminders_updates'),
					message_alerts = data.get('message_alerts'),
					user = user,
				)
			obj.save()
			return Response({'success' : "Successfully created"} , status = status.HTTP_200_OK)
		except Exception as e:
			return Response({'error':str(e)}, status = status.HTTP_400_BAD_REQUEST)


class EmailNotificationSettingDetails(APIView):

	def put(self, request, pk):
		data = request.data
		user = request.user
		
		try:
			notific_obj = EmailSetting.objects.get(Q(pk = pk) & Q(user = user))
			if data.has_key('monthlynews') and data.get('monthlynews') is not None:
				notific_obj.monthlynews = data.get('monthlynews')
			
			if data.has_key('productUpdate') and data.get('productUpdate') is not None:
				notific_obj.product_allyHealth_updates = data.get('productUpdate')
			
			if data.has_key('alerts_reminders') and data.get('alerts_reminders') is not None:
				notific_obj.alerts_reminders = data.get('alerts_reminders')
			
			if data.has_key('appointment_reminders_updates') and data.get('appointment_reminders_updates') is not None:
				notific_obj.appointment_reminders_updates = data.get('appointment_reminders_updates')
			
			if data.has_key('message_alerts') and data.get('message_alerts') is not None:
				notific_obj.message_alerts = data.get('message_alerts')
			
			notific_obj.save()
			
			return Response({'success' : "Successfully updated"} , status = status.HTTP_200_OK)
		except Exception as e:
			return Response({'error' : str(e)}, status = status.HTTP_400_BAD_REQUEST)







class PushNotificationSetting(APIView):

	
	def get(self,request):
		user = request.user
		try:
			push_obj = PushNotification.objects.filter(user = user)
			serialized = PushSettingSerializer(push_obj, many = True, context = {'request': request})
			return Response(serialized.data, status = status.HTTP_200_OK)  
		except Exception as e:
			return Response({'error':str(e)}, status = status.HTTP_400_BAD_REQUEST)

	def post(self, request):
		user = request.user
		data = request.data
	
		if (not data.has_key('productUpdate') and not data.get('productUpdate')):
			return Response({'error': "Please provide productUpdate"}, status = status.HTTP_400_BAD_REQUEST)

		if (not data.has_key('alerts_reminders') and not data.get('alerts_reminders')):
			return Response({'error': "Please provide alerts_reminders"}, status = status.HTTP_400_BAD_REQUEST)

		if (not data.has_key('appointment_reminders_updates') and not data.get('appointment_reminders_updates')):
			return Response({'error': "Please provide appointment_reminders_updates"}, status = status.HTTP_400_BAD_REQUEST)

		if (not data.has_key('message_alerts') and not data.get('message_alerts')):
			return Response({'error': "Please provide message_alerts"}, status = status.HTTP_400_BAD_REQUEST)
		try:
			obj = PushNotification.objects.create(
					productUpdate = data.get('productUpdate'),
					alerts_reminders = data.get('alerts_reminders'),
					appointment_reminders_updates = data.get('appointment_reminders_updates'),
					message_alerts = data.get('message_alerts'),
					user = user,
				)
			obj.save()
			return Response({'success' : "Successfully created"} , status = status.HTTP_200_OK)
		except Exception as e:
			return Response({'error':str(e)}, status = status.HTTP_400_BAD_REQUEST)


class PushNotificationSettingDetails(APIView):
	def put(self, request, pk):
		data = request.data
		user = request.user
		try:
			notific_obj = PushNotification.objects.get(Q(pk = user.id) & Q(user = user))
			if data.has_key('productUpdate') and data.get('productUpdate') is not None:
				notific_obj.productUpdate = data.get('productUpdate')
			
			if data.has_key('alerts_reminders') and data.get('alerts_reminders') is not None:
				notific_obj.alerts_reminders = data.get('alerts_reminders')
			
			if data.has_key('appointment_reminders_updates') and data.get('appointment_reminders_updates') is not None:
				notific_obj.appointment_reminders_updates = data.get('appointment_reminders_updates')
			
			if data.has_key('message_alerts') and data.get('message_alerts') is not None:
				notific_obj.message_alerts = data.get('message_alerts')
		
			notific_obj.save()
			return Response({'success' : "Successfully updated"} , status = status.HTTP_200_OK)
		except Exception as e:
			return Response({'error' : str(e)} , status = status.HTTP_400_BAD_REQUEST)

	
class SmsSettingApi(APIView):


	def get(self,request):
		user = request.user
		try:
			sms_obj = SmsSetting.objects.filter(user = user)
			serialized = SmsSettingSerializer(sms_obj, many = True, context = {'request': request})
			return Response(serialized.data, status = status.HTTP_200_OK)  
		except Exception as e:
			return Response({'error':str(e)}, status = status.HTTP_400_BAD_REQUEST)


	def post(self, request):
		user = request.user
		data = request.data
		try:
		
			if (not data.has_key('alerts_reminders') and not data.get('alerts_reminders')):
				return Response({'error': "Please provide alerts_reminders"}, status = status.HTTP_400_BAD_REQUEST)

			if (not data.has_key('appointment_reminders_updates') and not data.get('appointment_reminders_updates')):
				return Response({'error': "Please provide appointment_reminders_updates"}, status = status.HTTP_400_BAD_REQUEST)

			if (not data.has_key('message_alerts') and not data.get('message_alerts')):
				return Response({'error': "Please provide message_alerts"}, status = status.HTTP_400_BAD_REQUEST)
			
			obj = SmsSetting.objects.create(
					alerts_reminders = data.get('alerts_reminders'),
					appointment_reminders_updates = data.get('appointment_reminders_updates'),
					message_alerts = data.get('message_alerts'),
					user = user,
				)
			obj.save()
			return Response({'success' : "Successfully created"} , status = status.HTTP_200_OK)
		except Exception as e:
			return Response({'error':str(e)}, status = status.HTTP_400_BAD_REQUEST)


class SmsSettingDetails(APIView):

	def put(self, request, pk):
		data = request.data
		user = request.user

		try:
			notific_obj = SmsSetting.objects.get(Q(pk = pk) & Q(user = user))
			
			if data.has_key('alerts_reminders') and data.get('alerts_reminders') is not None:
				notific_obj.alerts_reminders = data.get('alerts_reminders')
			
			if data.has_key('appointment_reminders_updates') and data.get('appointment_reminders_updates') is not None:
				notific_obj.appointment_reminders_updates = data.get('appointment_reminders_updates')
			
			if data.has_key('message_alerts') and data.get('message_alerts') is not None:
				notific_obj.message_alerts = data.get('message_alerts')
			


			notific_obj.save()
			return Response({'success' : "Successfully updated"} , status = status.HTTP_200_OK)
		except Exception as e:
			return Response({'error' : str(e)}, status = status.HTTP_400_BAD_REQUEST)



