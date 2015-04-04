from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()
from yonetim.views import *
import yonetim.views 
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',ana_sayfa),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^about/',hakkinda),
    url(r'^contact/',iletisim),
    url(r'^past/',gecmis),
    url(r'^now/',simdi),
    url(r'^future/',gelecek),
    url(r'^yazilar/(?P<soru>\d+)/$', yonetim.views.sayfa, name='sayfa'),
    url(r'^testler/(?P<soru>\d+)/$',yonetim.views.test, name="test"),

    
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
