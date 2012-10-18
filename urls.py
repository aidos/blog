from django.conf.urls.defaults import *
from django.contrib import admin

handler500 = 'djangotoolbox.errorviews.server_error'

admin.autodiscover()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    ('^$', include('blog.urls')),
)
