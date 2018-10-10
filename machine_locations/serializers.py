from rest_framework import serializers

from machine_locations.models import MachineLocation


class MachineLocationSerializers(serializers.ModelSerializer):

    class Meta:
        model = MachineLocation
        fields = ('id', 'name', 'owner',)
