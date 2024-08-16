from django.urls import path
from .views import Respiracion_view #importar la view 

urlpatterns = [
    #path que es funcion para crear una url
    #1 como se va a localizar la url
    # 2. como aparece en la view y adicoional  se pone as_view(metodo que permite que se vea)
    # 3. nombre como la vamos a llamar la url en otros campos  
    path('respiracion/',Respiracion_view.as_view(), name='respiracion_instrucciones')
]