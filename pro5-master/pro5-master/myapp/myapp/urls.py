from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^myapp/', include('myapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'login.views.logout_page'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', 'login.views.register'),
    url(r'^register/success/$', 'login.views.register_success'),
    url(r'^home/$','login.views.home'),
    url(r'^about.html/$', 'login.views.about'),
    url(r'^blog.html/$', 'login.views.blog'),
    url(r'^contact.html/$', 'login.views.contact'),
    url(r'^details_ITCOcean.html/$', 'login.views.details_ITCOcean'),
    url(r'^details.html/$', 'login.views.details'),
    url(r'^details_cgin.html/$', 'login.views.details_cgin'),
    url(r'^details_coral.html/$', 'login.views.details_coral'),
    url(r'^details_fish.html/$', 'login.views.details_fish'),
    url(r'^details_forecast.html/$', 'login.views.details_forecast'),
    url(r'^details_sat.html/$', 'login.views.details_sat'),
    url(r'^details_storm.html/$', 'login.views.details_storm'),
    url(r'^details_storm2.html/$', 'login.views.details_storm2'),
    url(r'^details_warn.html/$', 'login.views.details_warn'),
    url(r'^service.html/$', 'login.views.service'),
    url(r'^recent_activities/$', 'sesmicinfo.views.recent_activities'),
    url(r'^showmarkers/$', 'sesmicinfo.views.showmarkers'),
    #url(r'^markers/$', 'sesmicinfo.views.showmarkers'),
)

