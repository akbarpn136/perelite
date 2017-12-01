from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api1/tugas/', views.Tugas.as_view()),
]
