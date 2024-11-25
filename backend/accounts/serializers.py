from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.core.exceptions import ValidationError as DjangoValidationError
from allauth.account import app_settings as allauth_account_settings
from allauth.utils import get_username_max_length
from allauth.account.models import EmailAddress
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from .models import UserProfile
from dj_rest_auth.serializers import UserDetailsSerializer

User = get_user_model()

class ProfileSerializer(UserDetailsSerializer):
    # class StockSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Genre
    #         fields = ('id', 'name',)    
  
    class Meta:
        model = UserProfile
        # 이 부분에 정의되는 부분만 수정 가능
        fields = ('investment_style', 'resolution', 'nickname', 'image')
        read_only_fields = ('investment_style',)  # 투자 성향은 테스트를 통해서만 변경 가능
        
class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_account_settings.USERNAME_MIN_LENGTH,
        required=allauth_account_settings.USERNAME_REQUIRED,
    )
    email = serializers.EmailField(required=allauth_account_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    nickname = serializers.CharField(max_length=40, required=True)

    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_account_settings.UNIQUE_EMAIL:
            if email and EmailAddress.objects.is_verified(email):
                raise serializers.ValidationError(
                    _('이미 등록된 이메일 주소입니다.'),
                )
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("비밀번호가 일치하지 않습니다."))
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
        }

    # def save(self, request):
    #     adapter = get_adapter()
    #     user = adapter.new_user(request)
    #     self.cleaned_data = self.get_cleaned_data()
    #     user = adapter.save_user(request, user, self, commit=False)
    #     if "password1" in self.cleaned_data:
    #         try:
    #             adapter.clean_password(self.cleaned_data['password1'], user=user)
    #         except DjangoValidationError as exc:
    #             raise serializers.ValidationError(
    #                 detail=serializers.as_serializer_error(exc)
    #             )
    #     user.save()
    #     self.custom_signup(request, user)
    #     setup_user_email(request, user, [])
        
    #     # UserProfile 생성 및 닉네임 저장
    #     user_profile = user.profile
    #     user_profile.nickname = self.cleaned_data.get('nickname')
    #     user_profile.save()
        
    #     return user
    
    def save(self, request):
        user = super().save(request)
        user.refresh_from_db()  # 프로필이 생성되었는지 확인하기 위해 데이터베이스에서 사용자 정보를 새로고침
        user.profile.nickname = self.cleaned_data.get('nickname')
        user.profile.save()
        
        return user