from django.conf.urls import url
from .views import *

urlpatterns = [
   url(r'^hol/', index_adop),
]