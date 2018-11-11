from django.conf.urls import url
from .views import index, weather, get_param

urlpatterns = [
    url(r"^index/$", index),
    url(r"^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$", weather),
    url(r"^get_param/$", get_param)
]
