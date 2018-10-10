from rest_framework import serializers

from machine_locations.serializers import MachineLocationSerializers
from unit_prices.models import UnitPrice


class UnitPriceSerializers(serializers.ModelSerializer):
    machine_location = MachineLocationSerializers(read_only=True)

    class Meta:
        model = UnitPrice
        fields = ('id', 'broadcasting_hours', 'renew', 'power_type', 'price', 'machine_location',)


class UnitPriceCreatingSerializers(serializers.ModelSerializer):

    class Meta:
        model = UnitPrice
        fields = ('id', 'broadcasting_hours', 'renew', 'power_type', 'price', 'machine_location',)


class UnitPriceInShortSerializers(serializers.ModelSerializer):

    class Meta:
        model = UnitPrice
        fields = ('id', 'price',)


class UnitPriceInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = UnitPrice
        fields = '__all__'

