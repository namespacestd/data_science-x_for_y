from django.conf.urls import patterns, include, url
from django.conf import settings 
from .utilities import AppInitialization
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'x_for_y.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'home.views.index', name='index'),
    url(r'^sign_up/', 'home.views.sign_up', name='sign_up'),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
AppInitialization.initialize_database()