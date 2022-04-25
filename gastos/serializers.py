from rest_framework import serializers
from gastos import models


class GastosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gastos
        fields = '__all__'