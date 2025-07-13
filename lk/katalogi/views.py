from django.shortcuts import render

from rest_framework import viewsets, permissions
from .serializers import NomenklaturaSerializer, GruppaNomenklaturySerializer
from .models import Nomenklatura, GruppaNomenklatury

from django.views.generic.list import ListView 

# Create your views here.
class NomenklaturaViewSet(viewsets.ModelViewSet):
    queryset = Nomenklatura.objects.all()
    serializer_class = NomenklaturaSerializer
    permission_classes = [permissions.IsAdminUser]



# Create your views here.
class GruppaNomenklaturyViewSet(viewsets.ModelViewSet):
    queryset = GruppaNomenklatury.objects.all()
    serializer_class = GruppaNomenklaturySerializer
    permission_classes = [permissions.IsAdminUser]

