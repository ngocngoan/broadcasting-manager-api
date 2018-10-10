from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from time_ranges import views

urlpatterns = [
    url(r'^time-ranges$', views.TimeRangeList.as_view()),
    url(r'^time-ranges/(?P<pk>[0-9]+)$', views.TimeRangeDetail.as_view()),
    url(r'^time-ranges/reports$', views.TimeRangeReport.as_view()),
    # url(r'^time-ranges/reports/month/(?P<month>(0?[1-9])|(1[0-2]))/year/(?P<year>((199[0-9])|(20[0-9][0-9])))$',
    #     views.TimeRangeByMonthReport.as_view()),
    url(r'^time-ranges/bills$', views.TimeRangeBillReport.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns,)
