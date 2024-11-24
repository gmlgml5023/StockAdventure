from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()

class ProfileSerializer(UserDetailsSerializer):
    # class StockSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Genre
    #         fields = ('id', 'name',)    
  
    class Meta:
        model = UserProfile
        # 이 부분에 정의되는 부분만 수정 가능('followings : 팔로워')
        fields = ('investment_style', 'resolution', 'nickname', 'image')
        read_only_fields = ('investment_style',)  # 투자 성향은 테스트를 통해서만 변경 가능