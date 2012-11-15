from django.conf.urls import patterns, include, url

from person.views import show

urlpatterns = patterns('',
    url(r'^(?P<name>[\w\d]+)', show, name="show_person"),
)
