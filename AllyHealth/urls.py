from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views

from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views


schema_view = get_swagger_view(title='AllyHealth API Documentation')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'docs/', include_docs_urls(title='AllyHealth API')),
    url(r'^salesforce/', include('SalesForce.urls')),
    url(r'^login/', views.obtain_auth_token),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^allyuser/', include('AllyUsers.urls')),
    url(r'^helpers/', include('Helpers.urls')),
    url(r'^mdlive/', include('Mdlive.urls')),
    url(r'swagger-docs/', schema_view),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


