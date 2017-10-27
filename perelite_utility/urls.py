from django.conf.urls import url
from . import butir

urlpatterns = [
    url(r'^api1/butir/$', butir.Butir.as_view()),
    url(r'^api1/butir/(?P<butir>\w.+)/$', butir.ButirModifikasi.as_view()),
]
