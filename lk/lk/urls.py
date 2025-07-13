"""
URL configuration for lk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include


from tseny.views import NomenklaturaView

# для JWT аутентификации (Часть 5)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# ---------------------

urlpatterns = [


    path('', NomenklaturaView.as_view(), name = 'index'),

    path('admin/', admin.site.urls),
    path('', include('users.urls')),

    # для JWT аутентификации (Часть 5)
    # Отправляем
    # {
    # "username": "1513069426",
    # "password": "321"
    # }
    # В ответ нам приходит аксесс токен и рефреш токен
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # для обновления токена (Часть 6)
    # Отправляем
    # {
    # "refresh": "<тут рефреш токен>"
    # }
    # В ответ нам приходит аксесс токен и рефреш токен тоже
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # ---------------------


    path('', include('katalogi.urls')), 
    path('', include('tseny.urls')),    

]
