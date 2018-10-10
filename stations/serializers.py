from rest_framework import serializers

from areas.serializers import AreaSerializers
from stations.models import Station
from televisions.serializers import TelevisionInShortSerializers


class StationSerializers(serializers.ModelSerializer):
    television = TelevisionInShortSerializers(read_only=True)
    area = AreaSerializers(read_only=True)

    class Meta:
        model = Station
        fields = '__all__'


class StationCreatingSerializers(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = '__all__'


class StationInShortSerializers(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = ('id', 'name',)
