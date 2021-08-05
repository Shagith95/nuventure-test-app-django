
from django.http import JsonResponse
from my_app.utils import get_nominatim_data


def get_address(request, lat, lon):
    data = get_nominatim_data(lat, lon)
    return JsonResponse(data)
