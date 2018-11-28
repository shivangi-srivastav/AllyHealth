from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, UserWallet
from SalesForce.models import CheckingSalesforceContact
from .serializers import CustomUserSerializer, ChangePasswordSerializer, UserWalletSerializers
from rest_framework.authtoken.models import Token
from Helpers.models import CategorydropdownValues, FileUpload
from django.contrib.auth.models import User
from rest_framework.generics import DestroyAPIView, UpdateAPIView, RetrieveAPIView
import traceback
import json
from rest_framework.permissions import IsAuthenticated
import sys
from django.conf import settings
from Mdlive.utlis import ssoAuth, mdliveReg, mdliveLoginApi
from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode
import base64
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .utlis import mdliveService

# Create your views here.

class UserCreate(APIView):
	""" 
	Creates the user. 
	"""

	permission_classes = ()

	def post(self,request,format=None):
		data = request.data
		try:
			if CustomUser.objects.filter(email = data.get('email')).exists():
				return Response({"error" : "This account has already been registered. If you have forgotten your username or password, please select the appropriate links for support."} , status = status.HTTP_400_BAD_REQUEST)
			
			if data.get('password') != data.get('paswd'):
				return Response({'error': "mdlive password must match"}, status = status.HTTP_400_BAD_REQUEST)
			
			crypt_pswd = base64.b64encode((encrypt(settings.EMAIL_CONFIG_ENCRYPTED_KEY, request.data.get('paswd',None))))
			
			# mdlive_token and mdlive_service_list
			try:
				mdlive_registration = mdliveReg(data,crypt_pswd)
			except Exception as e:
				return Response({'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)

			
			create_user = CustomUser.objects.create_user(
				email = data.get('email'),
				password=data.get('password'),
				)
		
			create_user.contact_number = data.get('contact_number')
			create_user.zipcode = data.get('zipcode')
			create_user.lastName = data.get('lastName')
			create_user.firstName = data.get('firstName')
			create_user.birthdate = data.get('birthdate')
			create_user.health_Insurance_Company = data.get('health_Insurance_Company')
			create_user.health_Insurance_Member_ID = data.get('health_Insurance_Member_ID')
			create_user.name = data.get('name')
			create_user.contact_Id = data.get('contact_Id')
			create_user.accountId = data.get('accountId')
			create_user.contact_CreatedDate = data.get('contact_CreatedDate')
			create_user.subscriber_id = data.get('subscriber_id')
			create_user.gender = data.get('gender')
			create_user.street = data.get('street')
			create_user.city = data.get('city')
			create_user.state = data.get('state')
			create_user.image = data.get('image')
			create_user.crypt_password = crypt_pswd
			create_user.save()
		
			# save mdlive user
			mdlive_registration.user = CustomUser.objects.get(email=create_user.email)
			mdlive_registration.save()

			# mdlive service api
			mdlive_service = mdliveService(data,create_user)

			token = Token.objects.get(user = create_user)
			return Response({'message': "user is created", "token": token.key}, status = status.HTTP_200_OK)
	
		except Exception as e:
			print str(e)
			return Response({'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)


class Me(APIView):
	"""
	user profile
	"""
	def get(self, request):
		user = request.user
		mdlive_tokn = mdliveLoginApi(user)
		serialized=CustomUserSerializer(user, context = {'request': request})
		return Response(serialized.data, status = status.HTTP_200_OK)  
		




class DeactivateProfile(APIView):
	"""
	deactivate user profile
	"""
	def get(self, request):
		user = request.user
		user.is_active = False
		user.save()
		return Response({'success': "deactivate profile"}, status = status.HTTP_200_OK)  
	

class DeleteDataView(APIView):
	permission_classes = ()
	def get(self,request):
		try:
			CustomUser.objects.get_all_users().delete()
			return Response({'success': True}, status = status.HTTP_200_OK)

		except Exception as e:
			return Response({'error': "Unable to delete"}, status = status.HTTP_400_BAD_REQUEST)



class UpdateProfileImage(APIView):
	"""
	update user image
	"""
	def put(self, request):
		logged_in_user = request.user
		data = request.data
		try:

			if not data.has_key('image') or not data.get('image'):
				return Response({'error': "Please provide image"}, status = status.HTTP_400_BAD_REQUEST)
			logged_in_user.image = data.get('image')
			logged_in_user.save()

			return Response({'success': "image is saved successfully"}, status = status.HTTP_200_OK)

		except Exception as e:
			return Response({'error': "Unable to update profile pic"}, status = status.HTTP_400_BAD_REQUEST)


class UpdateProfile(APIView):
	"""
	update user profile
	"""
	def put (self, request):
		data = request.data
		logged_in_user = request.user
		try:
			if data.has_key('zipcode') and data.get('zipcode') is not None:
				logged_in_user.zipcode = data.get('zipcode')

			if data.has_key('lastName') and data.get('lastName') is not None:
				logged_in_user.lastName = data.get('lastName')

			if data.has_key('birthdate') and data.get('birthdate') is not None:
				logged_in_user.birthdate = data.get('birthdate')

			if data.has_key('name') and data.get('name') is not None:
				logged_in_user.name = data.get('name')

			if data.has_key('gender') and data.get('gender') is not None:
				logged_in_user.gender = data.get('gender')

			if data.has_key('firstName') and data.get('firstName') is not None:
				logged_in_user.firstName = data.get('firstName')
				
			if data.has_key('street') and data.get('street') is not None:
				logged_in_user.street = data.get('street')

			if data.has_key('city') and data.get('city') is not None:
				logged_in_user.city = data.get('city')

			if data.has_key('state') and data.get('state') is not None:
				logged_in_user.state = data.get('state')

			if data.has_key('contact_number') and data.get('contact_number') is not None:
				logged_in_user.contact_number = data.get('contact_number')

			logged_in_user.save()

			return Response({'success': "Profile is updated successfully"}, status = status.HTTP_200_OK)

		except Exception as e:
			return Response({"error": "Unable to update profile"}, status = status.HTTP_400_BAD_REQUEST)



class UserCard(APIView):

	
	def post(self, request):
		data = request.data
		try:
			user = request.user
			if not data.has_key('front_image_id') or not data.get('front_image_id'):
				return Response({'error': "please provide front_image"}, status = status.HTTP_400_BAD_REQUEST)

			if not data.has_key('back_image_id') or not data.get('back_image_id'):
				return Response({'error': "please provide back_image"}, status = status.HTTP_400_BAD_REQUEST)

			if UserWallet.objects.filter(category = CategorydropdownValues.objects.filter(slug = data.get('category'))).exists():
				return Response({'error': "Duplicate entry for selected category"}, status = status.HTTP_400_BAD_REQUEST)


			obj = UserWallet.objects.create(
					category = CategorydropdownValues.objects.get(slug = data.get('category')) ,
					front = FileUpload.objects.get(pk = data.get('front_image_id')), 
					back = FileUpload.objects.get(pk = data.get('back_image_id')), 
					user = user)

			obj.is_currently_active = True
			obj.save()
			return Response({'success': " UserCard is saved"}, status = status.HTTP_200_OK)

		except Exception as e:
			return Response({"error": "Unable to save"}, status = status.HTTP_400_BAD_REQUEST)


	def get(self, request):
		try:
			user = request.user
			card_objs = UserWallet.objects.filter(user = user)
			serialized = UserWalletSerializers(card_objs, many = True, context = {'request': request})
			return Response(serialized.data, status = status.HTTP_200_OK)
		except Exception as e:
			return Response({'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)



class UserCardUpdate(APIView):
	"""
	update user card
	"""

	def put(self, request, walletid):
		try:

			data = request.data
			logged_in_user = request.user
			wallet_obj = UserWallet.objects.get(Q(user = logged_in_user) & Q(pk = walletid))

			if data.has_key('front'):
				file_obj = FileUpload.objects.get(pk = data.get('front'))
				wallet_obj.front = file_obj

			if data.has_key('back'):
				file_obj = FileUpload.objects.get(pk = data.get('back'))
				wallet_obj.back = file_obj

			wallet_obj.save()
			return Response({"success" : "Wallet is Updated"}, status = status.HTTP_200_OK)

		except Exception as e:
			return Response({'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)





class ChangePasswordView(UpdateAPIView):
 
	"""
	change password
	"""
	def put(self, request):
		data = request.data

		try:
			user = request.user

			new_password = data.get('new_password')
			old_password = data.get('old_password')

			if user.check_password(old_password):
				user.set_password(new_password)
				user.save()

				return Response({'success': "password has been changed"}, status = status.HTTP_200_OK)
			else:
				return Response({'error': "Old Password did not matched"}, status = status.HTTP_400_BAD_REQUEST)

		except Exception as e:
			return Response(str(e), status = status.HTTP_400_BAD_REQUEST)

