from django.conf.urls import patterns, include, url
from django.conf.urls import include

urlpatterns = patterns('',
    url(r'^', include('snippets.urls')),

)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
