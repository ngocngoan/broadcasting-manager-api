from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from unit_prices import views

urlpatterns = [
    url(r'^unit-prices$', views.UnitPriceList.as_view()),
    url(r'^unit-prices/(?P<pk>[0-9]+)$', views.UnitPriceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns,)
