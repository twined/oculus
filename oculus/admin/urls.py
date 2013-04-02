from django.conf.urls import patterns, url
from .views import IndexView, AJAXIndexView

urlpatterns = patterns(
    'admin',
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^hent/$', AJAXIndexView.as_view(), name="ajax-index"),
)
