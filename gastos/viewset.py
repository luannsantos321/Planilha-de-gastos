from rest_framework import viewsets
from gastos import serializers, models


class GastosViewset(viewsets.ModelViewSet):
    serializer_class = serializers.GastosSerializer
    queryset = models.Gastos.objects.all()