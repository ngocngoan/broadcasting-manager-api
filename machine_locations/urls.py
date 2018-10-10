from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from machine_locations import views

urlpatterns = [
    url(r'^machine-locations$', views.MachineLocationList.as_view()),
    url(r'^machine-locations/(?P<pk>[0-9]+)$', views.MachineLocationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns,)
