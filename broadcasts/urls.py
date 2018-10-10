from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from broadcasts import views

urlpatterns = [
    url(r'^broadcasts$', views.BroadcastList.as_view()),
    url(r'^broadcasts/(?P<pk>[0-9]+)$', views.BroadcastDetail.as_view()),
    url(r'^broadcasts/no-contract$', views.BroadcastWithNoContractList.as_view()),
    url(r'^broadcasts/channels$', views.BroadcastChannelsList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns,)
