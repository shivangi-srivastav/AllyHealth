from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json, requests
from .connection import connect_salesforce
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.exceptions import NotAcceptable, ValidationError
from . models import *
import urllib
from .utlis import *
from .serializers import CheckingSalesforceContactSerializer
from rest_framework import status
from AllyUsers.models import *
from rest_framework.permissions import IsAuthenticated
import traceback

	

class Redirecturlsalesforce(APIView):
	def post(self,request):
		pass
	def get(self, request):
		code = request.query_params.get('code')
		code_obj = SalesForceCode.objects.create(
			code = str(code))
		get_salesforce_tokens(code, code_obj)
		return Response({'success': "Code is saved"})



class GetCode(APIView):
	def get(self, request):
		code = connect_salesforce()
		return Response("hi")



# registration step
class SearchContactSalesForce(APIView):
	permission_classes = ()

	def post(self, request, format = None):
		data = request.data
		try:
			if not data.has_key('lastname') or  not data.get('lastname'):
				return Response({'error': "please provide lastname"}, status = status.HTTP_400_BAD_REQUEST)

			if not data.has_key('mailingPostalCode') or  not data.get('mailingPostalCode'):
				return Response({'error': "please provide zipcode"}, status = status.HTTP_400_BAD_REQUEST)

			if not data.has_key('birthdate') or  not data.get('birthdate'):
				return Response({'error': "please provide birthdate"}, status = status.HTTP_400_BAD_REQUEST)
				
			if CustomUser.objects.is_user_already_created(data.get('lastname'),data.get('mailingPostalCode'),data.get('birthdate')):
				return Response({"error": "This account has already been registered. If you have forgotten your username or password, please select the appropriate links for support."}, status = status.HTTP_400_BAD_REQUEST)


			data_response = searchcontact(data.get('lastname'),data.get('mailingPostalCode'),data.get('birthdate'))
			if type(data_response) == list:
				new_access_token()
				data_response = searchcontact(data.get('lastname'),data.get('mailingPostalCode'),data.get('birthdate'))
			
			if data_response.get('totalSize') == 0:
				return Response({'error': "Sorry, we couldn't locate this member. For help or assistance, call our support team during business hours at 888-565-3303."}, status = status.HTTP_400_BAD_REQUEST)

			return Response(data_response, status = status.HTTP_200_OK)
		except Exception  as e:
			return Response(str(e), status = status.HTTP_400_BAD_REQUEST)
