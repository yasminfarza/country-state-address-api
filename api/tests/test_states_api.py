from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Country, State

from api.serializers import StateSerializer


def states_url(country):
    """Return states By country URL"""
    return reverse('api:state-list', args=[country])


def sample_country():
    country = Country.objects.create(
        name='Bangladesh',
        latitude=23.6850,
        longitude=90.3563,
        code='BD'
    )

    return country


class PublicStatesApiTests(TestCase):
    """Test the publicly available states API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving states"""

        url = states_url(sample_country().name)
        res = self.client.get(url)
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

    def test_retrieve_states(self):
        """Test retrieving states"""

        self.country = sample_country()
        State.objects.create(
            name='Dhaka',
            country=self.country
        )
        State.objects.create(
            name='Chattagram',
            country=self.country
        )

        url = states_url(self.country.name)
        res = self.client.get(url)

        states = State.objects.filter(
            country__name=self.country.name).order_by('-name')
        serializer = StateSerializer(states, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
