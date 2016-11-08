from django.conf.urls import url,include
from .views import *


urlpatterns = [
    url(r'^hola/', index,name='index'),
    url(r'^nuevo/', MascotaCreateView.as_view(), name='mascota_crear'),
    url(r'^lista/', MascotaListView.as_view(), name='mascota_listar'),
    url(r'^editar/(?P<pk>\d+)/$',MascotaUpdateView.as_view(), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', MascotaDeleteView.as_view(), name='mascota_eliminar'),
]
