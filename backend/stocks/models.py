from django.db import models

# Create your models here.
# stock/models.py
from django.db import models

class Stock(models.Model):
    stock_id = models.CharField(max_length=6, primary_key=True)  # 종목코드
    stock_name = models.CharField(max_length=100)  # 종목명
    current_price = models.IntegerField(null=True)  # 종가
    price_change = models.IntegerField(null=True)  # 등락
    price_change_rate = models.FloatField(null=True)  # 등락율
    volume = models.BigIntegerField(null=True)  # 거래량
    trading_value = models.BigIntegerField(null=True)  # 거래대금
    market_cap = models.BigIntegerField(null=True)  # 시가총액
    issued_shares = models.BigIntegerField(null=True)  # 발행주식수
    
    week_change_rate = models.FloatField(null=True)  # 1주간
    month_change_rate = models.FloatField(null=True)  # 1개월간
    year_change_rate = models.FloatField(null=True)  # 1년간
    three_year_change_rate = models.FloatField(null=True)  # 3년간
    
    beta = models.FloatField(null=True)  # 베타
    debt_ratio = models.FloatField(null=True)  # 부채비율
    reserve_ratio = models.FloatField(null=True)  # 유보율
    revenue_growth_rate = models.FloatField(null=True)  # 매출액증가율
    eps_growth_rate = models.FloatField(null=True)  # EPS증가율
    roa = models.FloatField(null=True)  # ROA
    roe = models.FloatField(null=True)  # ROE
    eps = models.FloatField(null=True)  # EPS
    bps = models.FloatField(null=True)  # BPS
    per = models.FloatField(null=True)  # PER
    pbr = models.FloatField(null=True)  # PBR
    ev_ebitda = models.FloatField(null=True)  # EV/EBITDA
    revenue = models.BigIntegerField(null=True)  # 매출액
    sector = models.CharField(max_length=100)  # 업종
    sector_per = models.FloatField(null=True)  # 업종평균PER

    class Meta:
        db_table = 'stock'
        
    def __str__(self):
        return f"{self.stock_name} ({self.stock_id})"