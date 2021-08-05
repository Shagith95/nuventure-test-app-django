from django.urls import re_path
from my_app.views import get_address

urlpatterns = [
    re_path(r'^get_address/(?P<lat>[-?][\d]+[\.][\d]+)/(?P<lon>[-?][\d]+[\.][\d]+)/$', get_address, name='get_address'),
]
