from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from areas import views

urlpatterns = [
    url(r'^areas$', views.AreaList.as_view()),
    url(r'^areas/(?P<pk>[0-9]+)$', views.AreaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns,)
