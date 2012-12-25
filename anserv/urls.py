from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^event$', 'an_evt.views.handle_event'),
    url(r'^view/([a-z_]+)/([a-z_]+)$', 'an_evt.views.handle_view'), 
    url(r'^view/([a-z_]+)/([a-z_]+)/([a-z_0-9]+)$', 'an_evt.views.handle_view'), 
    url(r'^view/([a-z_]+)/([a-z_]+)/([a-z_0-9]+)/([a-z_0-9]+)$', 'an_evt.views.handle_view'), 
    url(r'^query$', 'an_evt.views.handle_query'),
    url(r'^list$', 'an_evt.views.handle_list'),
    url(r'^list/([a-z_]+)$', 'an_evt.views.handle_list'),
    url(r'^list/([a-z_]+)/([a-z_]+)$', 'an_evt.views.handle_list'),
    url(r'^list/([a-z_]+)/([a-z_]+)/([a-z_]+)$', 'an_evt.views.handle_list'),
    # url(r'^anserv/', include('anserv.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
