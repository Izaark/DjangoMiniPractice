from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^hola/', index,name='index'),
    url(r'^nuevo/', mascota_view, name='mascota_crear'),
    url(r'^lista/', MascotaListView.as_view(), name='mascota_listar'),
    url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar'),
]
