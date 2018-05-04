from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^hello/$', 'app.views.hello'),
                       url(r'^index/$', 'app.views.index', name='index'),
                       url(r'^home/(\d+)/$', 'app.views.home', name='home'),
                       url(r'^upload/$', 'app.views.upload', name='upload'),
                       url(r'^uploadfile/$', 'app.views.uploadfile', name='uploadfile'),
                       url(r'^highchart/(\d+)/$', 'app.views.highchart', name='highchart'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
