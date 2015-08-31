from django.conf.urls import patterns, include, url

urlpatterns = patterns('kappa.home.views',
    url(r'^$', 'home', name='home'),

)
