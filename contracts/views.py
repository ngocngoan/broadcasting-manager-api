from rest_framework import generics, filters
from rest_framework.renderers import JSONRenderer
from django_filters.rest_framework import DjangoFilterBackend

from contracts.models import Contract
from contracts.serializers import ContractSerializers, ContractCreatingSerializers


class ContractList(generics.ListCreateAPIView):
    queryset = Contract.objects.all().order_by('-id')
    serializer_class = ContractSerializers
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('broadcast',)
    filter_fields = ('broadcast',)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ContractCreatingSerializers
        return super(ContractList, self).get_serializer_class()


class ContractDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all().order_by('-id')
    serializer_class = ContractSerializers
    renderer_classes = (JSONRenderer,)

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return ContractCreatingSerializers
        return super(ContractDetail, self).get_serializer_class()
