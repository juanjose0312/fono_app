from django.urls import path
from .views import Discriminacion_auditiva_escoger_view
from .views import Discriminacion_auditiva_seleccionar_view

urlpatterns = [
    path(
        'discriminacion_auditiva_escoger/',
        Discriminacion_auditiva_escoger_view.as_view(),
        name='discriminacion_auditiva_escoger'
    ),
    path(
        'discriminacion_auditiva_seleccionar/',
        Discriminacion_auditiva_seleccionar_view.as_view(),
        name='discriminacion_auditiva_seleccionar'
    )
]
