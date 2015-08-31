from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kappa.views.home', name='home'),
    url(r'', include('kappa.home.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
