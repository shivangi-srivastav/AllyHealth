from django.conf.urls import url, include
from .views import *


urlpatterns = [
	url(r'^fileupload/$', Fileupload.as_view() ),

	url(r'^dropdownmasterfaqs/$', FAQList.as_view()),
	url(r'^dropdownmasterfaqs/(?P<masterslug>[-\w]+)/$', FAQSValues.as_view()),
	url(r'^dropdownmasterfaqs/(?P<masterslug>[-\w]+)/(?P<valueslug>[-\w]+)/$', FAQSValuesDetail.as_view()),

	url(r'^reviews/(?P<masterslug>[-\w]+)/$', CustomerReviewValues.as_view()),
	url(r'^reviews/(?P<masterslug>[-\w]+)/(?P<valueslug>[-\w]+)/$', CustomerReviewDetail.as_view()),

	url(r'^card/(?P<masterslug>[-\w]+)/$', CardValues.as_view()),
	url(r'^card/(?P<masterslug>[-\w]+)/(?P<valueslug>[-\w]+)/$', CardDetail.as_view()),

	url(r'^emailNotificationlistview/$', EmailNotificationSetting.as_view() ),
	url(r'^emailNotificationdetailview/(?P<pk>[0-9]+)/$', EmailNotificationSettingDetails.as_view() ),
	

	url(r'^pushNotificationlistview/$', PushNotificationSetting.as_view() ),
	url(r'^pushNotificationdetailview/(?P<pk>[0-9]+)/$', PushNotificationSettingDetails.as_view() ),

	url(r'^smsNotificationlistview/$', SmsSettingApi.as_view() ),
	url(r'^smsNotificationdetailview/(?P<pk>[0-9]+)/$', SmsSettingDetails.as_view() ),

	]


