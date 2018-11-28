import urllib
from django.conf import settings
import requests
import json
from .models import *
from AllyUsers.models import *
import base64
from simplecrypt import encrypt, decrypt
from rest_framework.exceptions import NotAcceptable
from base64 import b64encode, b64decode
from AllyUsers.models import CustomUser
def mdliveReg(data,crypt_pswd):
	"""
	Registered with mdlive
	"""
	
	token_dict = mdliveAuth()
	token = token_dict.get('jwt')
	registered_url = settings.MDLIVE_BASE_URL + "api/v1/patients"
	decode = decrypt(settings.EMAIL_CONFIG_ENCRYPTED_KEY,base64.b64decode(crypt_pswd))

	if data.get('gender') == 'M':
		gender_str = 'male'
	else:
		gender_str = 'female'

	headers = {"Authorization":"Bearer " + token,"Content-Type":"application/json"}
	
	payload = {
				"patient": {
				"first_name" : data.get('firstName'),
				"last_name"  : data.get('lastName'),
				"username"   : data.get('email'),
				"email"      : data.get('email'),
				"password"   : decode,
				"password_confirmation" : decode,
				"phone" : data.get('contact_number'),
				"zip" : data.get('zipcode'),
				"gender" : gender_str,
				"birthdate" : data.get('birthdate'),
				"affiliation_id" : "96",
				}
	}
	
	payload_json = json.dumps(payload)
	r = requests.post(registered_url, headers = headers, data = payload_json)
	response = json.loads(r.content)

	
	if response.has_key('errors') == True:
		error_response = response.get('errors')[0]
		raise NotAcceptable(error_response)
	
	create_mdlive_reg = MdliveRegistration.objects.create(
		m_patient_id = response.get('patient').get('id'),
		m_first_name = response.get('patient').get('first_name'),
		m_last_name = response.get('patient').get('last_name'),
		m_middle_name = response.get('patient').get('middle_name'),
		m_username = response.get('patient').get('username'),
		m_address1 = response.get('patient').get('address1'),
		m_address2 = response.get('patient').get('address2'),
		m_phone = response.get('patient').get('phone'),
		m_work_phone =  response.get('patient').get('work_phone'),
		m_affiliation_id =  96,
		m_jwt_token = response.get('patient').get('jwt_token'),
		m_istoken = response.get('token')[0],
		m_token1 = response.get('token')[1][0],
		m_token2 = response.get('token')[1][1] ,

	)
	
	create_mdlive_reg.save()
	return create_mdlive_reg



def mdliveAuth():
	"""
	Finding jwt token
	"""
	registered_url = settings.MDLIVE_BASE_URL + "auth/auth_token"
	headers = {"Content-Type":"application/json"}

	payload = {
		"auth":
			{
				"api_key":settings.MDLIVE_CREDENTIALS['api_key'],
				"password":settings.MDLIVE_CREDENTIALS['api_password']
			}

	}
	payload_json = json.dumps(payload)
	r = requests.post(registered_url, headers=headers, data = payload_json)
	response = json.loads(r.content)
	

	# saving app auth token"
	if MdliveAppAuth.objects.filter(slug = "mdlive_app_auth_token").exists():
		obj = MdliveAppAuth.objects.get(slug = "mdlive_app_auth_token")
		obj.jwt_auth = response.get('jwt')
		obj.save()
	else:
		MdliveAppAuth.objects.create(
			slug = "mdlive_app_auth_token",
			jwt_auth = response.get('jwt')
			)

	return response



def ssoAuth(data,create_user):
	"""
	User sso_token
	"""
	
	# token_dict = mdliveAuth()
	# token = token_dict.get('jwt')
	
	registered_url = settings.MDLIVE_BASE_URL + "api/v1/sso_auth/auth_token"
	
	headers = {"Content-Type":"application/json"}
	payload = { 
		"auth": 
		{
			"first_name": data.get('firstName'),
			"last_name": data.get('lastName'),
			"gender": data.get('gender'),
			"birthdate": data.get('birthdate'),
			"subscriber_id": "a0q3400000BoNoQAAV",
			"member_id": data.get('mdlive_id'),
			"phone": data.get('contact_number'),
			"email":  data.get('email'),
			"address1": data.get('street'),
			"city": data.get('city'),
			"state": data.get('state'),
			"zip": data.get('zipcode'),
			"relationship": data.get('relationship'),
		},
		"org": 
		{
			"ou": "AllyHealth"
		},
		"api": 
		{
			"api_key":settings.MDLIVE_CREDENTIALS['api_key'],
			"password":settings.MDLIVE_CREDENTIALS['api_password']
		}

	}
	
	payload_json = json.dumps(payload)
	r = requests.post(registered_url, headers = headers, data = payload_json)
	response = json.loads(r.content)

	create_sso_token = MdliveUserToken.objects.create(user = create_user,
	m_jwt_token = response.get('jwt'),
	m_patient_id = response.get('user').get('id'),
	user_type = response.get('user').get('type'),
	user_time_to_live_minutes = response.get('user').get('time_to_live_minutes')
	)
	create_sso_token.save()
	return response



def ssoAuthExtend():

	'''
	extending user_token validity
	'''

	token_dict = ssoAuth()
	token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOjY0MjE2NzUzNiwidXNlcm5hbWUiOiJNRExJVkUtNmFkYjcxZmUtNGFmOS00NDdiLWEwY2ItMzYxMjVkOWQ2OGJhIiwiYXBpX2NyZWRfaWQiOjQ2MywiZXhwIjoxNTM5MDg1NDc0fQ.GdUWsiSEkLeQaIdEi-KkCamkM7d1tcb0Tkv8w4SBm54"
	
	registered_url = settings.MDLIVE_BASE_URL + "api/v1/sso_auth/auth_extend"

	headers = {"Authorization":"Bearer " + token,"Content-Type":"application/json"}
	payload = { 
		
     "org": {
            "ou": "AllyHealth"
       },
         "api": {
       "api_key":settings.MDLIVE_CREDENTIALS['api_key'],
		"password":settings.MDLIVE_CREDENTIALS['api_password']
		}

	}
	
	payload_json = json.dumps(payload)
	r = requests.post(registered_url, headers = headers, data = payload_json)
	response = json.loads(r.content)
	return response



def mdliveLoginApi(user):
	"""
	mdlive login 
	"""

	

	decode_password = decrypt(settings.EMAIL_CONFIG_ENCRYPTED_KEY,base64.b64decode(user.crypt_password))
	registered_url = settings.MDLIVE_BASE_URL + "api/v1/mobile_user_auth/auth_token/"

	headers = {"Content-Type":"application/json"}
	payload = {
		  "auth": {
		    "username": user.email,
		    "password": decode_password
		  },
		  "device": {
		    "os": "Android"
		  },
		  "app": {
		    "app_id": "MDLIVE",
		    "current_version": "1051"
		  },
		  "api": {
		  	"username":settings.MDLIVE_CREDENTIALS['api_key'],
			"password":settings.MDLIVE_CREDENTIALS['api_password']
		  }
}
	
	payload_json = json.dumps(payload)
	r = requests.post(registered_url, headers = headers, data = payload_json)
	response = json.loads(r.content)
	# update user profile
	
	update_token = MdliveRegistration.objects.get(user = user)
	update_token.m_patient_id = response.get('user').get('id')
	update_token.m_jwt_token = response.get('jwt')
	update_token.save()
	return response