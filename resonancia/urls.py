from django.urls import path
from .views import ResonanciaView

urlpatterns = [

    # this is a example of a path by juan jose
    path('resonancia/', ResonanciaView.as_view(), name='resonancia'),
]