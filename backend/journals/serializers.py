from rest_framework import serializers
from .models import Journal

# 매매일지 목록
class JournalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('id', 'transaction_date', 'buysell')


# 단일 매매일지
class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'
        