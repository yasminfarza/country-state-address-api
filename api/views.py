from rest_framework import viewsets

from core.models import Country
from api import serializers


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    """List of country"""
    queryset = Country.objects.all()
    serializer_class = serializers.CountrySerializer

    def get_queryset(self):
        """Retrieve the country for the api"""
        name = self.request.query_params.get('name')
        code = self.request.query_params.get('code')
        queryset = self.queryset
        if name:
            queryset = queryset.filter(name=name)
        if code:
            queryset = queryset.filter(code=code)

        return queryset
