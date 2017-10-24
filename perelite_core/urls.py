from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api1/', views.Butir.as_view()),
]
