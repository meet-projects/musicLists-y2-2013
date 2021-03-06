from django.conf.urls import patterns, include, url
from music import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^signUp/$', views.showSignUp),
	url(r'^loginsubmit/$',views.submitlogin),
	url(r'^submitsignup/$',views.signup),
	url(r'^profile/$',views.profile),
	url(r'^addsong/$',views.addsong),
	url(r'^homepage/$', views.homepage),
	url(r'^logout/$', views.logout_user),
	url(r'^showaddsong/$', views.showaddsongs),
	url(r'^makepost/$', views.add_post),
	url(r'^addartist/$', views.addartist),
	url(r'^showaddartist/$', views.showaddartist),
	url(r'^addalbum/$', views.addalbum),
	url(r'^showaddalbum/$', views.showaddalbum),
    # url(r'^musicLists/', include('musicLists.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
