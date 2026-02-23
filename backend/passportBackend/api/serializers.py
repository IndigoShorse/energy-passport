from rest_framework import serializers

from .models import EnergyPassportDetail


class EnergyPassportDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyPassportDetail
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}  # ID будет автоматически генерироваться
        }
