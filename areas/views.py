from rest_framework import generics, viewsets
from rest_framework.renderers import JSONRenderer

from areas.models import Area
from areas.serializers import AreaSerializers


class AreaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializers
    renderer_classes = (JSONRenderer,)


class AreaList(generics.ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializers
    renderer_classes = (JSONRenderer,)


class AreaDetail(generics.RetrieveAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializers
    renderer_classes = (JSONRenderer,)
