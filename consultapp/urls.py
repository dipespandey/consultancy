from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from consultapp import views


app_name = 'consultapp'
urlpatterns = [
        url(r'^post/$', views.PostList.as_view(), name='post-list'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post-detail'),

]
