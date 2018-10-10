from rest_framework import serializers

from broadcasts.serializers import BroadcastInShortSerializers
from contracts.models import Contract
from unit_prices.serializers import UnitPriceInShortSerializers


class ContractSerializers(serializers.ModelSerializer):
    broadcast = BroadcastInShortSerializers(read_only=True)
    unit_price = UnitPriceInShortSerializers(read_only=True)

    class Meta:
        model = Contract
        fields = '__all__'


class ContractCreatingSerializers(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'


class ContractInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

