from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(FAQdropdownMaster)


class dropdownMasterAdmin(admin.ModelAdmin):
	list_display = ('id','dropdownmaster','question', 'slug')

admin.site.register(FAQdropdownValues, dropdownMasterAdmin)
admin.site.register(CustomerReview)
admin.site.register(CategorydropdownValues)
admin.site.register(EmailSetting)
admin.site.register(PushNotification)
admin.site.register(SmsSetting)
admin.site.register(FileUpload)



