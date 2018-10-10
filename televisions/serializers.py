from rest_framework import serializers

from televisions.models import Television


class TelevisionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Television
        fields = '__all__'


class TelevisionInShortSerializers(serializers.ModelSerializer):

    class Meta:
        model = Television
        fields = ('id', 'name')
