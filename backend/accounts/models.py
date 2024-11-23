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

    def __str__(self):
        return f"{self.user.username}의 프로필"