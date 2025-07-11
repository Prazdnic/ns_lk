from django.urls import path, include
from .views import *
from rest_framework import routers

# в этом куске кода уже включены и описаны все пути CRUD-операций (Create, Read, Update, Delete). В view тоже подобный кусок, который все описывает
router_perem = routers.DefaultRouter()
router_perem.register(r'api/v1/users', CustomUser_Viewha, basename='users') # basename - добавили после того, как добавили api/v1/user. Типа когда записей register больше одной - приходится добавлять basename

# отправляем токен и нам возвращаются наши данные о пользователе
# [
#     {
#         "username": "1513069426",
#         "full_name": "ООО \"Клиника Аура\" 111",
#         "status": "COMP"
#     }
# ]
# После того, как в Часть 6 переписали ProfileCustomUser_Viewha стало так. Низамов сказал, что это так нужно для фронтенда что бы это не значило
# {
#     "user": {
#         "username": "1513069426",
#         "full_name": "ООО \"Клиника Аура\" 111",
#         "status": "COMP"
#     }
# }
router_perem.register(r'api/v1/user', ProfileCustomUser_Viewha, basename='user')

urlpatterns = [
    path('', include(router_perem.urls)),

    # для того, чтобы разлогиниться (Часть 6)
    # Отправляем
    # {
    # "refresh": "<тут рефреш токен>" 
    # }
    # В ответ нам приходит аксесс токен и рефреш токен тоже
    path('api/v1/user_logout/', LogoutView.as_view(), name='user_logout')
]
# ---------- 
