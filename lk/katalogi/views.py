from django.shortcuts import render

from rest_framework import viewsets, permissions
from .serializers import NomenklaturaSerializer, GruppaNomenklaturySerializer, KartinkiSerializer
from .models import Nomenklatura, GruppaNomenklatury, Kartinki

from .mixins import MyModelViewSet

""" # Create your views here.
class NomenklaturaViewSet(viewsets.ModelViewSet):
    queryset = Nomenklatura.objects.all()
    serializer_class = NomenklaturaSerializer
    permission_classes = [permissions.IsAdminUser]



# Create your views here.
class GruppaNomenklaturyViewSet(viewsets.ModelViewSet):
    queryset = GruppaNomenklatury.objects.all()
    serializer_class = GruppaNomenklaturySerializer
    permission_classes = [permissions.IsAdminUser] """


# Сделали миксины. В чем кардинальная разница пока что непонятно
class NomenklaturaViewSet(MyModelViewSet):
    queryset = Nomenklatura.objects.all()
    serializer_class = NomenklaturaSerializer
  

# Create your views here.
class GruppaNomenklaturyViewSet(MyModelViewSet):
    queryset = GruppaNomenklatury.objects.all()
    serializer_class = GruppaNomenklaturySerializer
  

class ImagesViewSet(MyModelViewSet):
    queryset = Kartinki.objects.all()
    serializer_class = KartinkiSerializer