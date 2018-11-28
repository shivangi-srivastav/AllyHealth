from .models import *
from rest_framework import serializers
from Mdlive.models import MdliveRegistration, MdliveAppAuth, MdliveUserToken


class MdliveRegistrationSerializer(serializers.ModelSerializer):

	class Meta:
		model = MdliveRegistration
		fields = ('id','m_patient_id','m_first_name','m_last_name','m_middle_name','m_username'
					,'m_address1','m_address2','m_phone','m_work_phone','m_affiliation_id','m_jwt_token','m_istoken','m_token1','m_token2')

class MdliveUserTokenSerializer(serializers.ModelSerializer):
	class Meta:
		model = MdliveUserToken
		fields = ('m_jwt_token','user_id','user_type','user_time_to_live_minutes','m_patient_id',)





class MdliveAppAuthSerializer(serializers.ModelSerializer):
	class Meta:
		model = MdliveAppAuth
		fields = ('jwt_auth')


class MdliveServiceApiSerializer(serializers.ModelSerializer):
	class Meta:
		model = MdliveServiceApi
		fields = ('personal_health','health_wellness_coaching','consult_a_specialist','talk_to_a_counselor','talk_to_a_doctor')




class CustomUserSerializer(serializers.ModelSerializer):
	# mdlive_user = serializers.SerializerMethodField()
	mdlive_user = serializers.SerializerMethodField()
	api_token = serializers.SerializerMethodField()
	mdlive_service_api = serializers.SerializerMethodField()
	

	class Meta:
		model  = CustomUser
		fields = ('id',
				'email',
				'contact_number',
				'zipcode',
				'lastName',
				'birthdate',
				'name',
				'subscriber_id',
				'gender',
				'street',
				'city',
				'state',
				'image',
				'is_active',
				'firstName',
				
				'api_token',
				'mdlive_service_api',
				'mdlive_user'
				
			)
	
	
	def get_api_token(self, obj):
		auth = MdliveAppAuth.objects.get(slug = "mdlive_app_auth_token")
		return auth.jwt_auth

	
	def get_mdlive_service_api(self, obj):
		mdlive_ser = MdliveServiceApi.objects.get(user = obj.id)
		serializer = MdliveServiceApiSerializer(mdlive_ser)
		return serializer.data


	def get_mdlive_user(self, obj):
		mdlive_ser = MdliveRegistration.objects.get(user = obj.id)
		serializer = MdliveRegistrationSerializer(mdlive_ser)
		return serializer.data

class ChangePasswordSerializer(serializers.Serializer):
	old_password = serializers.CharField(required=True)
	new_password = serializers.CharField(required=True)



class UserWalletSerializers(serializers.ModelSerializer):
	class Meta:
		model = UserWallet
		fields = ('id','category','front','back')
		depth = 1