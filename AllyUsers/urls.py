from django.conf.urls import url, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
		url(r'^', include('django.contrib.auth.urls')),
		url(r'^createuser/$', UserCreate.as_view()),
        url(r'^userprofile/$', Me.as_view()),
        url(r'^profileupdate/$', UpdateProfile.as_view()),
        url(r'^user_delete/$', DeleteDataView.as_view()),
        url(r'^updateprofilepic/$', UpdateProfileImage.as_view()),
		url(r'^createWalletCard/$', UserCard.as_view()),
		url(r'^createWalletCard/(?P<walletid>[0-9]+)/$', UserCardUpdate.as_view()),
		url(r'^ChangePassword/$', ChangePasswordView.as_view()),
		url(r'^deactivate/$', DeactivateProfile.as_view()),

]