from django.db import models
from django.contrib.auth.models import User
from investment_style.models import InvestmentStyle

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    investment_style = models.ForeignKey(
        InvestmentStyle,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='투자 성향'
    )
    resolution = models.TextField(blank=True, default="주식 투자로 부자되기")
    nickname = models.CharField(max_length=40, blank=True)
    image = models.ImageField(upload_to='images/', default='images/default_character.png')
    
    def __str__(self):
        return f"{self.user.username}의 프로필"
    
    # UserProfile이 존재하지 않을 경우 새로 생성
    @classmethod
    def get_or_create(cls, user):
        try:
            return cls.objects.get(user=user)
        except cls.DoesNotExist:
            return cls.objects.create(user=user)