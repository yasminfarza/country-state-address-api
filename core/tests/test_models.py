from django.test import TestCase
from core import models


def sample_country():
    country = models.Country.objects.create(
        name='Bangladesh',
        latitude=23.6850,
        longitude=90.3563,
        code='BD'
    )

    return country


class CountryModelTests(TestCase):

    def setUp(self):
        self.country = sample_country()

    def test_country_str_represent(self):
        """Test the country string represent"""

        self.assertEqual(str(self.country), self.country.name)

    def test_country_model_fields(self):
        """Test the country model fields"""

        self.assertIsInstance(self.country.name, str)
        self.assertIsInstance(self.country.latitude, float)
        self.assertIsInstance(self.country.longitude, float)
        self.assertIsInstance(self.country.code, str)


class StateModelTests(TestCase):

    def setUp(self):
        self.country = sample_country()
        self.state = models.State.objects.create(
            name='Dhaka',
            country=self.country
        )

    def test_state_str_represent(self):
        """Test the state string represent"""

        self.assertEqual(str(self.state), self.state.name)

    def test_state_model_fields(self):
        """
            Test the state model fields and
            each state associated with a country
        """

        self.assertIsInstance(self.state.name, str)
        self.assertEqual(self.country, self.state.country)


class AddressModelTests(TestCase):

    def setUp(self):
        self.country = sample_country()
        self.state = models.State.objects.create(
            name='Dhaka',
            country=self.country
        )
        self.address = models.Address.objects.create(
            name='Rampura',
            house_number='06',
            road_number=5,
            state=self.state
        )

    def test_address_str_represent(self):
        """Test the address string represent"""

        self.assertEqual(str(self.address), self.address.name)

    def test_address_model_fields(self):
        """
            Test the address model fields and
            each address associated with state
        """

        self.assertIsInstance(self.address.name, str)
        self.assertIsInstance(self.address.house_number, str)
        self.assertIsInstance(self.address.road_number, int)
        self.assertEqual(self.state, self.address.state)
