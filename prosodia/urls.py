from django.urls import path
from .views import ProsodiaCancionAPIView, ProsodiaTrabalenguasAPIView

urlpatterns = [
    path(
        'prosodia_cancion/',
        ProsodiaCancionAPIView.as_view(),
        name='prosodia_cancion'
    ),
    path(
        'prosodia_trabalenguas/',
        ProsodiaTrabalenguasAPIView.as_view(),
        name='prosodia_trabalenguas'
    )
]