
import json
from unittest import mock
from datetime import timedelta

from django.utils import timezone
from django.conf import settings
from django.core.cache import cache
from django.test import TestCase, override_settings

from my_app.utils import get_nominatim_data, CACHE_TIMEOUT

GET_ADDRESS_DATA = {"name": "Test Address, City, State, Code, Country"}


@override_settings(CACHES={'default': settings.TEST_CACHE})
class TestGetAddress(TestCase):
    expected_response = GET_ADDRESS_DATA
    lat = 0
    lon = 0
    cache_key = '0_0'
    cache = cache

    @mock.patch('my_app.utils.fetch_nominatim')
    def call_get_address(self, mock_fetch_nominatim):
        '''
        Call address fetch function with mock response
        '''
        mock_fetch_nominatim.return_value = GET_ADDRESS_DATA
        response = get_nominatim_data(self.lat, self.lon)
        return response

    def set_cache_entry(self):
        '''
        Add entry to cache to simulate already existing data
        '''
        self.cache.set(self.cache_key, json.dumps(self.expected_response), CACHE_TIMEOUT)

    def test_value_not_present_in_cache(self):
        '''
        Test caching with no data present in cache
        '''
        response = self.call_get_address()
        self.assertEqual(response, self.expected_response)

    def test_value_present_in_cache(self):
        '''
        Test caching with data present in cache
        '''
        self.set_cache_entry()
        response = self.call_get_address()
        self.assertEqual(response, self.expected_response)

    def test_value_cleared_after_cache_expiry(self):
        '''
        Test caching with data present in cache but read after expiry time
        '''
        self.set_cache_entry()
        mock_time = timezone.now() + timedelta(hours=25)
        with mock.patch('django.utils.timezone.now', return_value=mock_time):
            response = self.call_get_address()
        self.assertEqual(response, self.expected_response)

    def tearDown(self):
        '''
        Clear cache
        '''
        self.cache.clear()
