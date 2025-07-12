import uuid

from rest_framework import serializers
from .models import Nomenklatura, GruppaNomenklatury

class NomenklaturaSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(default = uuid.uuid4) # Опять переопределили

    class Meta:
        model = Nomenklatura
        fields = ['id', 'polnoe_naimenovanie', 'roditel']



class GruppaNomenklaturySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(default = uuid.uuid4) # Опять переопределили

    class Meta:
        model = GruppaNomenklatury
        fields = ['id', 'naimenovanie', 'roditel']
