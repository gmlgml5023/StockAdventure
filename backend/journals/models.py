from django.db import models
from django.conf import settings

# Create your models here.
class Journal(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='journals'
    )
    stock_name = models.CharField(max_length=20)            # 종목명
    transaction_date = models.DateField()                   # 거래날짜
    buysell = models.CharField(max_length=2,                # 거래유형 (매수, 매도)
                               choices=(('매수', '매수'),
                                        ('매도', '매도')))
    quantity = models.IntegerField()                        # 거래수량
    price = models.IntegerField()                           # 거래가격
    reason = models.TextField()                             # 매매이유
    feedback = models.TextField()                           # 피드백