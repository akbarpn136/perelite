from django.conf.urls import url
from . import butir, personil

urlpatterns = [
    url(r'^api1/butir/$', butir.Butir.as_view()),
    url(r'^api1/butir/(?P<kategori>\w+)/$', butir.Butir.as_view()),
    url(r'^api1/butir/(?P<butir>\w.+)/modifikasi/$', butir.ButirModifikasi.as_view()),

    url(r'^api1/personil/$', personil.Personil.as_view()),
    url(r'^api1/personil/(?P<username>\w+)/$', personil.PersonilModifikasi.as_view()),
]
