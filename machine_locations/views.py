from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from machine_locations.models import MachineLocation
from machine_locations.serializers import MachineLocationSerializers


class MachineLocationList(generics.ListAPIView):
    queryset = MachineLocation.objects.all()
    serializer_class = MachineLocationSerializers
    renderer_classes = (JSONRenderer,)


class MachineLocationDetail(generics.RetrieveAPIView):
    queryset = MachineLocation.objects.all()
    serializer_class = MachineLocationSerializers
    renderer_classes = (JSONRenderer,)
