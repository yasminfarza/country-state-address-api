from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Country

from api.serializers import CountrySerializer

COUNTRIES_URL = reverse('api:country-list')


class PublicCountryApiTests(TestCase):
    """Test the publicly available country API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving countries"""

        res = self.client.get(COUNTRIES_URL)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class PrivateCountryApiTests(TestCase):
    """Test the authorized user country API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@gmail.com',
            'test123345'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_countries(self):
        """Test retrieving countries"""

        Country.objects.create(
            name='Bangladesh',
            latitude=23.6850,
            longitude=90.3563,
            code='BD'
        )
        Country.objects.create(
            name='Australia',
            latitude=45.6850,
            longitude=34.3563,
            code='AU'
        )

        res = self.client.get(COUNTRIES_URL)

        countries = Country.objects.all().order_by('-name')
        serializer = CountrySerializer(countries, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
