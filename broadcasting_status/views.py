from rest_framework import generics, filters
from rest_framework.renderers import JSONRenderer
from django_filters.rest_framework import DjangoFilterBackend

from broadcasting_status.models import BroadcastingStatus
from broadcasting_status.serializers import BroadcastingStatusSerializers, BroadcastingStatusYearsSerializers


class BroadcastingStatusList(generics.ListCreateAPIView):
    queryset = BroadcastingStatus.objects.all().order_by('-id')
    serializer_class = BroadcastingStatusSerializers
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('name',)
    filter_fields = ('name', 'station',)


class BroadcastingStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BroadcastingStatus.objects.all().order_by('-id')
    serializer_class = BroadcastingStatusSerializers
    renderer_classes = (JSONRenderer,)


class BroadcastingStatusYears(generics.ListAPIView):
    serializer_class = BroadcastingStatusYearsSerializers
    queryset = BroadcastingStatus.objects.dates('date', 'year')
    renderer_classes = (JSONRenderer,)
