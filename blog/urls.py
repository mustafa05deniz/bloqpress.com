from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()
from views import *
urlpatterns = patterns('',
    
    
    
    url(r'^$',ana_sayfa),
    
    
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
