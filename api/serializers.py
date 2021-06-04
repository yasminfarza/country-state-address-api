from rest_framework import serializers

from core.models import Country


class CountrySerializer(serializers.ModelSerializer):
    """Serializer for Country objects"""

    class Meta:
        model = Country
        fields = ('id', 'name', 'latitude', 'longitude', 'code')
        read_only = True
