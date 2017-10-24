from django.conf.urls import url
from . import butir

urlpatterns = [
    url(r'^api1/butir/$', butir.Butir.as_view()),
]
