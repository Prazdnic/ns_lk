from rest_framework import serializers
from .models import Tseny

class TsenySerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='nomenklatura.polnoe_naimenovanie')

    class Meta:
        model = Tseny
        fields = ['id', 'nomenklatura', 'title', 'tsena']