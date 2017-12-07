from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api1/tugas/$', views.Tugas.as_view()),
    url(r'^api1/tugas/(?P<kategori>\w+)/$', views.Tugas.as_view()),
    url(r'^api1/tugas/(?P<tugas_id>\w+)/rincian/$', views.TugasModifikasi.as_view()),
]
