from django.db import models

class InvestmentStyle(models.Model):
    INVESTMENT_TYPES = [
        (1, '안정형 투자자'),
        (2, '위험중립형 투자자'),
        (3, '공격투자형 투자자'),
    ]
    
    style_id = models.AutoField(primary_key=True)
    style_name = models.IntegerField(
        choices=INVESTMENT_TYPES,
        help_text='1: 안정형 투자자, 2: 위험중립형 투자자, 3: 공격투자형 투자자'
    )

    class Meta:
        db_table = 'investment_style'