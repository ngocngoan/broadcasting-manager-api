from rest_framework import serializers

from broadcasting_status.models import BroadcastingStatus


class BroadcastingStatusSerializers(serializers.ModelSerializer):

    class Meta:
        model = BroadcastingStatus
        fields = '__all__'


class BroadcastingStatusYearsSerializers(serializers.ModelSerializer):
    year = serializers.SerializerMethodField('get_all_years')

    @staticmethod
    def get_all_years(obj):
        return obj.year

    class Meta:
        model = BroadcastingStatus
        fields = ('year',)
