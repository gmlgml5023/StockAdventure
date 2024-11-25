# stock/serializers.py
from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):
    is_liked = serializers.SerializerMethodField()
    like_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Stock
        fields = '__all__'

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False