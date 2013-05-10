from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
# TODO: test pattern

    url(r'^map/$', 'api.views.test_static', name='static_map'),
    # Examples:
    # url(r'^$', 'yandexmaps2.views.home', name='home'),
    # url(r'^yandexmaps2/', include('yandexmaps2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
