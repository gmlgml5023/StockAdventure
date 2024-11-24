from django.db import models


class InvestmentStyle(models.Model):
    STYLE_TYPES = [
        (1, '안정형 투자자'),
        (2, '위험중립형 투자자'),
        (3, '공격투자형 투자자'),
    ]
     
    style_id = models.IntegerField(primary_key=True, choices = STYLE_TYPES, verbose_name = '투자 성향 스타일') # '1: 안정형 투자자, 2: 위험중립형 투자자, 3: 공격투자형 투자자'
    name = models.CharField(max_length=100,  default='Default Style', verbose_name='투자 성향 이름')   
     
    def __str__(self):
        return self.get_style_id_display()
    
class StyleQuestion(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='질문')
    
    def __str__(self):
        return self.question_text
    
class StyleChoice(models.Model):
    question = models.ForeignKey(StyleQuestion, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200, verbose_name='선택항목')
    style_points = models.IntegerField(default=0, verbose_name='스타일 점수')
    
    def __str__(self):
        return self.choice_text