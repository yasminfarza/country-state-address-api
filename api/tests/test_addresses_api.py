from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Country, State, Address

from api.serializers import AddressSerializer, AddressDetailSerializer

ADDRESS_URL = reverse('api:address-list')


def address_state_url(state):
    """Return address By state URL"""
    return reverse('api:address-states', args=[state])


def details_url(address_id):
    """Return address detail URL"""
    return reverse('api:address-detail', args=[address_id])


def sample_country():
    country = Country.objects.create(
        name='Bangladesh',
        latitude=23.6850,
        longitude=90.3563,
        code='BD'
    )

    return country


def sample_address(state):
    """Create and return a sample address"""
    address = Address.objects.create(
        name='Rampura',
        house_number='04',
        road_number=32,
        state=state
    )

    return address


class PublicAddressApiTests(TestCase):
    """Test the publicly available addresses API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving addresses"""

        res = self.client.get(ADDRESS_URL)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class PrivateStatesApiTests(TestCase):
    """Test the authorized country API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@gmail.com',
            'test123345'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

        self.country = sample_country()
        self.state = State.objects.create(
            name='Dhaka',
            country=self.country
        )

    def test_retrieve_addresses(self):
        """Test retrieving all addresses"""

        Address.objects.create(
            name='Banani',
            house_number='06',
            road_number=5,
            state=self.state
        )
        sample_address(self.state)

        res = self.client.get(ADDRESS_URL)

        addresses = Address.objects.all().order_by('-name')
        serializer = AddressSerializer(addresses, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_addresses_By_State(self):
        """Test retrieving addresses by state"""

        sample_address(self.state)

        url = address_state_url(self.state.name)
        res = self.client.get(url)

        addresses = Address.objects.filter(
            state__name=self.state.name).order_by('-name')
        serializer = AddressSerializer(addresses, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_view_address_detail(self):
        """Test viewing a address detail"""

        address = sample_address(self.state)

        url = details_url(address.id)
        res = self.client.get(url)

        serializer = AddressDetailSerializer(address)
        self.assertEqual(res.data, serializer.data)
