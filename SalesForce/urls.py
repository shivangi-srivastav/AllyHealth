from django.conf.urls import url,include
from .views import *
urlpatterns = [

	# url(r'^redirecturl/', Redirecturlsalesforce.as_view()),
	url(r'^signupstep/', SearchContactSalesForce.as_view(), name='step1'),
    # url(r'^getcode/', GetCode.as_view()),
    
]