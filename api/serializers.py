from rest_framework import serializers

from core.models import Country, State, Address


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


class AddressSerializer(serializers.ModelSerializer):
    """Serializer for Address objects"""

    state = serializers.StringRelatedField()

    class Meta:
        model = Address
        fields = ('id', 'name', 'house_number', 'road_number', 'state')


class AddressDetailSerializer(AddressSerializer):
    """Serializer for details of address"""

    def to_representation(self, instance):
        rep = super(AddressDetailSerializer, self).to_representation(instance)
        rep['country'] = Country.objects.get(state=instance.state).name
        return rep
