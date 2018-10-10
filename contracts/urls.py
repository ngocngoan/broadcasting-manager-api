from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from contracts import views

urlpatterns = [
    url(r'^contracts$', views.ContractList.as_view()),
    url(r'^contracts/(?P<pk>[0-9]+)$', views.ContractDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns,)
