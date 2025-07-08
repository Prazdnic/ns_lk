from django.urls import path, include
from .views import *
from rest_framework import routers

# в этом куске кода уже включены и описаны все пути CRUD-операций (Create, Read, Update, Delete). В view тоже подобный кусок, который все описывает
router_perem = routers.DefaultRouter()
router_perem.register(r'api/v1/users', CustomUser_Viewha)

urlpatterns = [
    path('', include(router_perem.urls)),
]
#----------

# Тест 123

# Тест 321