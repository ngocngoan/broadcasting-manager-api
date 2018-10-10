from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from broadcasting_status import views

urlpatterns = [
    url(r'^broadcasting-status$', views.BroadcastingStatusList.as_view()),
    url(r'^broadcasting-status/(?P<pk>[0-9]+)$', views.BroadcastingStatusDetail.as_view()),
    url(r'^broadcasting-status/years$', views.BroadcastingStatusYears.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns,)
