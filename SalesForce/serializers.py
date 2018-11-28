from .models import *
from rest_framework import serializers


class CheckingSalesforceContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = CheckingSalesforceContact
		fields = ('email_r','contact_number_r','zipcode_r','lastName_r','birthdate_r','health_Insurance_Company_r',
			'health_Insurance_Member_ID_r','name_r','contact_Id_r','accountId_r','contact_CreatedDate_r','subscriber_id_r')

