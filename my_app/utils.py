
import json
import requests
from xml.etree import ElementTree
from django.core.cache import cache

NOMINATIM_ENDPOINT = 'https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}'
CACHE_TIMEOUT = 60 * 60 * 24


def fetch_nominatim(lat, lon):
    url = NOMINATIM_ENDPOINT.format(lat=str(lat), lon=str(lon))
    response = requests.get(url)
    xml = ElementTree.fromstring(response.content)
    name_tag = xml.find('.//result')
    if not name_tag:
        return {'error': 'No data found'}
    data = {
        'name': name_tag.text
    }
    return data


def get_nominatim_data(lat, lon):
    cache_key = f"{lat}_{lon}"
    data = cache.get(cache_key)
    if data:
        data = json.loads(data)
    else:
        data = fetch_nominatim(lat, lon)
        if data.get('name'):
            cache.set(cache_key, json.dumps(data), CACHE_TIMEOUT)
    return data
