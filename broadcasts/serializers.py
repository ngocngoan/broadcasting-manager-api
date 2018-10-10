from rest_framework import serializers

from stations.serializers import StationInShortSerializers, StationSerializers
from broadcasts.models import Broadcast


class BroadcastSerializers(serializers.ModelSerializer):
    station = StationInShortSerializers(read_only=True)

    class Meta:
        model = Broadcast
        fields = '__all__'


class BroadcastCreatingSerializers(serializers.ModelSerializer):

    class Meta:
        model = Broadcast
        fields = '__all__'


class BroadcastStationSerializers(serializers.ModelSerializer):
    station = StationSerializers(read_only=True)

    class Meta:
        model = Broadcast
        fields = '__all__'


class BroadcastInShortSerializers(serializers.ModelSerializer):

    class Meta:
        model = Broadcast
        fields = ('id', 'name',)


class BroadcastChannelsInShortSerializers(serializers.ModelSerializer):

    class Meta:
        model = Broadcast
        fields = ('name',)


class BroadcastInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Broadcast
        fields = '__all__'

