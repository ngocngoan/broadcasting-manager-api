from rest_framework import serializers

from broadcasts.models import Broadcast
from broadcasts.serializers import BroadcastStationSerializers, BroadcastInfoSerializers
from contracts.models import Contract
from contracts.serializers import ContractInfoSerializers
from televisions.models import Television
from televisions.serializers import TelevisionSerializers
from time_ranges.models import TimeRange
from unit_prices.models import UnitPrice
from unit_prices.serializers import UnitPriceInfoSerializers


class TimeRangeSerializers(serializers.ModelSerializer):

    class Meta:
        model = TimeRange
        fields = '__all__'


class TimeRangeMonthlyReportSerializers(serializers.ModelSerializer):
    broadcast = serializers.SerializerMethodField('get_broadcast_detail')
    duration = serializers.SerializerMethodField('get_duration_time')
    type = serializers.SerializerMethodField('get_broadcast_type')

    @staticmethod
    def get_broadcast_detail(obj):
        broadcast_detail = Broadcast.objects.get(pk=obj['broadcasting_status__broadcast_id'])
        return BroadcastStationSerializers(broadcast_detail, read_only=True).data

    @staticmethod
    def get_duration_time(obj):
        return obj['duration']

    @staticmethod
    def get_broadcast_type(obj):
        return obj['type']

    class Meta:
        model = TimeRange
        fields = ('broadcast', 'type', 'duration',)


class TimeRangeBillSerializers(serializers.ModelSerializer):
    television = serializers.SerializerMethodField('get_television_detail')
    payments = serializers.SerializerMethodField('get_payments_detail')

    @staticmethod
    def get_television_detail(obj):
        television_detail = Television.objects.get(pk=obj['television'])
        return TelevisionSerializers(television_detail, read_only=True).data

    @staticmethod
    def get_payments_detail(obj):
        for payment in obj['payments']:
            broadcast_detail = Broadcast.objects.get(pk=payment['broadcast'])
            contract_detail = Contract.objects.get(pk=payment['contract'])
            unit_price_detail = UnitPrice.objects.get(pk=payment['unit_price'])
            payment['broadcast'] = BroadcastInfoSerializers(broadcast_detail, read_only=True).data
            payment['contract'] = ContractInfoSerializers(contract_detail, read_only=True).data
            payment['unit_price'] = UnitPriceInfoSerializers(unit_price_detail, read_only=True).data
        return obj['payments']

    class Meta:
        model = TimeRange
        fields = ('television', 'payments',)

