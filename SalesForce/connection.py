
from simple_salesforce import Salesforce
import json, requests
import datetime
from django.conf import settings


def connect_salesforce():
	client_id = settings.SALESFORCE_CREDENTIALS['client_id']
	client_secret = settings.SALESFORCE_CREDENTIALS['client_secret']
	redirect_uri = settings.SALESFORCE_CREDENTIALS['redirect_uri']	
	try:
		r = requests.post('https://login.salesforce.com/services/oauth2/authorize?response_type=code',data={
			'client_id':client_id,
			'redirect_uri':redirect_uri,
			})

		
		return r
	except Exception as e:
		print str(e)
		# re validat here
		
