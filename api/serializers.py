from rest_framework import serializers

from core.models import Country, State


class CountrySerializer(serializers.ModelSerializer):
    """Serializer for Country objects"""

    class Meta:
        model = Country
        fields = ('id', 'name', 'latitude', 'longitude', 'code')


class StateSerializer(serializers.ModelSerializer):
    """Serializer for State objects"""

    country = serializers.StringRelatedField()

    class Meta:
        model = State
        fields = ('id', 'name', 'country')
