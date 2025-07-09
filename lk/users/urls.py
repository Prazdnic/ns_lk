from django.urls import path, include
from .views import *
from rest_framework import routers

# в этом куске кода уже включены и описаны все пути CRUD-операций (Create, Read, Update, Delete). В view тоже подобный кусок, который все описывает
router_perem = routers.DefaultRouter()
router_perem.register(r'api/v1/users', CustomUser_Viewha, basename='users') # basename - добавили после того, как добавили api/v1/user. Типа когда записей register больше одной - приходится добавлять basename
router_perem.register(r'api/v1/user', ProfileCustomUser_Viewha, basename='user')

urlpatterns = [
    path('', include(router_perem.urls)),
]
# ---------- 
