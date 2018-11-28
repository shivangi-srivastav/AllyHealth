from .models import MdliveServiceApi, CustomUser
from .views import *







def mdliveService(data,create_user):
	
	mdlive_service = MdliveServiceApi.objects.create(
		user = create_user,
		personal_health = data.get('personalHealth'),
		health_wellness_coaching = data.get('healthwellness_coaching'),
		consult_a_specialist = data.get('consulSspecialist'),
		talk_to_a_counselor = data.get('talk_to_counselor'),
		talk_to_a_doctor = data.get('talk_to_doctor'),
	)
	
	mdlive_service.save()
	return mdlive_service