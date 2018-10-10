from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from televisions import views

urlpatterns = [
    url(r'^televisions$', views.TelevisionList.as_view()),
    url(r'^televisions/(?P<pk>[0-9]+)$', views.TelevisionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns,)
