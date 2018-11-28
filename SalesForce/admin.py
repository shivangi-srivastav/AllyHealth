from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(SalesForceCode)
admin.site.register(SalesForceTokens)
admin.site.register(ResuableAccessToken)
admin.site.register(CheckingSalesforceContact)



