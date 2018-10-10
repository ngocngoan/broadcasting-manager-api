from rest_framework import generics, filters
from rest_framework.renderers import JSONRenderer
from django_filters.rest_framework import DjangoFilterBackend

from broadcasts.models import Broadcast
from broadcasts.serializers import BroadcastSerializers, BroadcastCreatingSerializers, \
    BroadcastChannelsInShortSerializers


class BroadcastList(generics.ListCreateAPIView):
    queryset = Broadcast.objects.all().order_by('-id')
    serializer_class = BroadcastSerializers
    renderer_classes = (JSONRenderer,)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('name',)
    filter_fields = ('name', 'station',)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BroadcastCreatingSerializers
        return super(BroadcastList, self).get_serializer_class()


class BroadcastDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Broadcast.objects.all().order_by('-id')
    serializer_class = BroadcastSerializers
    renderer_classes = (JSONRenderer,)

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return BroadcastCreatingSerializers
        return super(BroadcastDetail, self).get_serializer_class()


class BroadcastWithNoContractList(generics.ListCreateAPIView):
    """
    listing Broadcasts without no contacts
    """
    queryset = Broadcast.objects.filter(is_by_contract=True).all()
    serializer_class = BroadcastSerializers


class BroadcastChannelsList(generics.ListCreateAPIView):
    """
    listing Channels in Broadcasts
    """
    queryset = Broadcast.objects.values('name').distinct('name')
    serializer_class = BroadcastChannelsInShortSerializers
    renderer_classes = (JSONRenderer,)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    filter_fields = ('is_by_region',)
