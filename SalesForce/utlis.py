
import urllib
from django.conf import settings
import requests
import json
from .models import *
# def soqlEscape(someString):
#     return someString.replace("\\", "\\\\").replace("'", "\\'")


def searchcontact(lastname, postalcode, dob):
	token = get_access_token()
	lastname = lastname.strip()
	postalcode = postalcode.strip()
	dob = dob
	base_url = settings.SALESFORCE_BASE_URL
	query_url = "query/?q=SELECT+Id,LastName,MailingPostalCode,Emergency_Contact_Number__c,Birthdate,CreatedDate,FirstName, MailingCity,Account.Name, MailingState, MailingStreet, Gender__c, AccountId,MobilePhone,Email,Name,(SELECT Id ,Enrollment_Date__c ,Personal_Health_Ally__c, Talk_to_a_Doctor_Now_MDLIVE__c, Relationship__c, Consult_a_Specialist__c, MDLIVE_ID__c, Talk_to_a_Counselor__c,Health_Wellness_Coaching__c,Health_Insurance_Member_ID__c, Health_Insurance_Company__c FROM Contact.Subscribers__r )+from+Contact+WHERE+LastName+=+'"+ lastname +"' +AND+MailingPostalCode+=+'" + postalcode + "'+AND+Birthdate+=+"+ dob +""
	headers = {"Authorization":"Bearer " + token,"Content-Type":"application/json"}
	request_url = base_url + query_url
	r = requests.get(request_url, headers = headers)
	res = json.loads(r.content)

	return res





# don't change any thing of this function
def get_salesforce_tokens(code, code_obj):
	
	encoded_code = urllib.urlencode({'code': code})
	base_url  =  "https://login.salesforce.com/services/oauth2/token?grant_type=authorization_code&"
	base_url = base_url + str(encoded_code)
	base_url = base_url + "&client_id=" + str(settings.SALESFORCE_CREDENTIALS['client_id'])
	base_url = base_url + "&client_secret=" + str(settings.SALESFORCE_CREDENTIALS['client_secret'])
	base_url = base_url + "&redirect_uri=https://allyhealth.theclientdemos.com/salesforce/redirecturl/"
	r = requests.post(url = base_url)
	response = json.loads(r.content)

	if response.has_key('error'):
		pass
	else:
		

		access_token = response.get('access_token', None)
		refresh_token = response.get('refresh_token', None)
		signature = response.get('signature', None)
		ess_token = response.get('access_token', None)
		id_token = response.get('id_token', None)
		issued_at = response.get('issued_at', None)
		instance_url = response.get('instance_url', None)


		# create model instance

		sales_force_credentials_obj = SalesForceTokens.objects.create(
			access_token = access_token,
			refresh_token = refresh_token,
			signature = signature,
			id_token = id_token,
			instance_url = instance_url,
			of_code =  code_obj,
			issued_at = issued_at 
			)

	return True


def new_access_token():
	instance_obj = SalesForceTokens.objects.get(is_active = True)

	refresh_token = instance_obj.refresh_token

	# made request for new access token

	base_url = "https://login.salesforce.com/services/oauth2/token?grant_type=refresh_token&client_id="
	base_url = base_url +  str(settings.SALESFORCE_CREDENTIALS['client_id'])
	base_url = base_url + "&client_secret=" + str(settings.SALESFORCE_CREDENTIALS['client_secret'])
	base_url = base_url + "&refresh_token=" + str(refresh_token)
	r = requests.post(url = base_url)

	response =  json.loads(r.content)

	if response.has_key('error'):
		pass
	else:
		access_token = response.get('access_token', None)


		# get the previous access token 
		resubale_obj = ResuableAccessToken.objects.get(pk = 1)
		resubale_obj.resuable_access_token
		resubale_obj.resuable_access_token = access_token
		resubale_obj.save()

	return resubale_obj.resuable_access_token


def get_access_token():
	resubale_obj = ResuableAccessToken.objects.get(pk = 1)
	return resubale_obj.resuable_access_token



























