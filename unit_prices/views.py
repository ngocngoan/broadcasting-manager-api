from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from unit_prices.models import UnitPrice
from unit_prices.serializers import UnitPriceSerializers, UnitPriceCreatingSerializers


class UnitPriceList(generics.ListCreateAPIView):
    queryset = UnitPrice.objects.all().order_by('-id')
    serializer_class = UnitPriceSerializers
    renderer_classes = (JSONRenderer,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UnitPriceCreatingSerializers
        return super(UnitPriceList, self).get_serializer_class()


class UnitPriceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnitPrice.objects.all().order_by('-id')
    serializer_class = UnitPriceSerializers
    renderer_classes = (JSONRenderer,)

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UnitPriceCreatingSerializers
        return super(UnitPriceDetail, self).get_serializer_class()
