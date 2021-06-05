
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Country, State, Address
from api import serializers


class BaseAttrViewSet():
    """Manage Base attribute"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CountryViewSet(BaseAttrViewSet,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
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


class StateViewSet(BaseAttrViewSet,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
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


class AddressViewSet(BaseAttrViewSet,
                     viewsets.ReadOnlyModelViewSet):
    """List of address"""
    queryset = Address.objects.all()
    serializer_class = serializers.AddressSerializer

    def get_serializer_class(self):
        """Return appropriate serializer"""
        if self.action == 'retrieve':
            return serializers.AddressDetailSerializer

        return self.serializer_class

    @action(methods=['get'], detail=False, url_path='states/(?P<state>[^/.]+)',
            url_name='states')
    def states_action(self, request, **kwargs):
        """ Get addresses by state """
        queryset = self.queryset.filter(state__name=kwargs['state'])

        """ Filter by house number and road number """
        house_number = request.query_params.get('house_number')
        road_number = request.query_params.get('road_number')

        if house_number:
            queryset = queryset.filter(house_number=house_number)
        if road_number:
            queryset = queryset.filter(road_number=road_number)

        serializer = self.serializer_class(queryset, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
