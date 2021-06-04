from rest_framework import viewsets

from core.models import Country, State
from api import serializers


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    """List of countries"""
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


class StateViewSet(viewsets.ReadOnlyModelViewSet):
    """List of states by country"""
    queryset = State.objects.all()
    serializer_class = serializers.StateSerializer

    def get_queryset(self):
        """Retrieve the state for the api"""
        name = self.request.query_params.get('name')
        if 'country' in self.kwargs:
            queryset = self.queryset.filter(
                country__name=self.kwargs['country'])
        if name:
            queryset = queryset.filter(name=name)

        return queryset
