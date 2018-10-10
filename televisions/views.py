from rest_framework import generics, filters, permissions
from rest_framework.renderers import JSONRenderer
from django_filters.rest_framework import DjangoFilterBackend

from televisions.models import Television
from televisions.serializers import TelevisionSerializers


class TelevisionList(generics.ListCreateAPIView):
    queryset = Television.objects.all().order_by('-id')
    serializer_class = TelevisionSerializers
    renderer_classes = (JSONRenderer,)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('name',)
    filter_fields = ('name', 'phone_number',)
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class TelevisionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Television.objects.all().order_by('-id')
    serializer_class = TelevisionSerializers
    renderer_classes = (JSONRenderer,)
