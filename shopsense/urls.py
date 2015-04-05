from django.conf.urls import url
from shopsense import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^movies/$', views.MovList.as_view()),
    url(r'^movies/(?P<pk>[0-9]+)/$', views.MovDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)
