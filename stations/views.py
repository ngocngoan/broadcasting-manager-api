from rest_framework import generics, filters
from rest_framework.renderers import JSONRenderer
from django_filters.rest_framework import DjangoFilterBackend

from stations.models import Station
from stations.serializers import StationSerializers, StationCreatingSerializers


class StationList(generics.ListCreateAPIView):
    queryset = Station.objects.all().order_by('-id')
    serializer_class = StationSerializers
    renderer_classes = (JSONRenderer,)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('name',)
    filter_fields = ('name',)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return StationCreatingSerializers
        return super(StationList, self).get_serializer_class()


class StationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all().order_by('-id')
    serializer_class = StationSerializers
    renderer_classes = (JSONRenderer,)

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return StationCreatingSerializers
        return super(StationDetail, self).get_serializer_class()

