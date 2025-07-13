from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/v1/products', NomenklaturaViewSet, basename = 'products')
router.register(r'api/v1/products_group', GruppaNomenklaturyViewSet, basename = 'products_group')
router.register(r'api/v1/images', ImagesViewSet, basename = 'images')


urlpatterns = [
   path('', include(router.urls)),    
]
