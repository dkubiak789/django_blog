from django.conf.urls import patterns, include, url

from django.contrib import admin
from post import urls as post_urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^post/', include(post_urls)),
)
