from rest_framework import serializers
from .models import InvestmentStyle

class InvestmentStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentStyle
        fields = ['style_id', 'style_name']