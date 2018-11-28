from django.conf.urls import url,include
from .views import *
urlpatterns = [

	
	# url(r'^mdlive_register/', MdliveRegistered.as_view() ),
	url(r'^MdliveAuth/', MdliveAuth.as_view()),
	url(r'^mdlive_login/', MdliveLogin.as_view() ),
	# url(r'^MdliveUserToken/', MdliveUserToken.as_view() ),
]