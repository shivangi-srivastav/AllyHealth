from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.conf import settings
import requests
import json
import urllib
from .utlis import *
import traceback

# Create your views here.


# class MdliveRegistered(APIView):
# 	print(APIView)
# 	permission_classes = ()
	
# 	def post(self, request):
# 		user = request.user
# 		print (user)
# 		try:
# 			if not CustomUser.objects.filter(email = user).exists():
# 				return Response({'error': "user not registered in salesforce"}, status = status.HTTP_400_BAD_REQUEST)
# 			else:
				
# 				mdlive_reg = CustomUser.objects.get(email = user)
# 				data = mdliveReg(mdlive_reg)
			
			
# 			create_mdlive_reg = MdliveRegistration.objects.create(user = user,

# 				m_patient_id = data.get('patient').get('id'),
# 				m_first_name = data.get('patient').get('first_name'),
# 				m_last_name = data.get('patient').get('last_name'),
# 				m_middle_name = data.get('patient').get('middle_name'),
# 				m_username = data.get('patient').get('username'),
# 				m_address1 = data.get('patient').get('address1'),
# 				m_address2 = data.get('patient').get('address2'),
# 				m_phone = data.get('patient').get('phone'),
# 				m_work_phone =  data.get('patient').get('work_phone'),
# 				m_affiliation_id =  96,
# 				m_jwt_token = data.get('patient').get('jwt_token'),
# 				m_istoken = data.get('token')[0].title(),
# 				m_token1 = data.get('token')[1][0],
# 				m_token2 = data.get('token')[1][1] ,
			
# 				)
# 			create_mdlive_reg.save()
# 			return Response(data,status = status.HTTP_200_OK)

# 		except Exception as e:
# 			print(str(e))
# 			print traceback.print_exc()

# 			return Response({'error': "already register, please login"}, status = status.HTTP_400_BAD_REQUEST)


class MdliveLogin(APIView):
	permission_classes = ()

	def get(self, request):
		user = request.user
		try:
			mdlive_login = mdliveLoginApi(user)
			return Response(mdlive_login, status = status.HTTP_201_CREATED)
		except Exception as e:
			return Response({'error': "User not exists with this credentials"}, status = status.HTTP_400_BAD_REQUEST)
		




class MdliveAuth(APIView):
	permission_classes = ()

	def post(self, request):
		try:
			data = mdliveAuth()
			return Response(data,status = status.HTTP_201_CREATED)
		except Exception as e:
			return Response({'error': "auth error"}, status = status.HTTP_400_BAD_REQUEST)


	

# class MdliveUserToken(APIView):
# 	permission_classes = ()

# 	def post(self, request):
# 		try:
# 			if data == 'errorCode':
# 				data = ssoAuthExtend()
# 				return Response(data,status = status.HTTP_201_CREATED)
# 			else:
# 				data = ssoAuth()
# 				return Response(data,status = status.HTTP_201_CREATED)
			
			
# 		except Exception as e:
# 			return Response(str(e), status = status.HTTP_400_BAD_REQUEST)
	
		
