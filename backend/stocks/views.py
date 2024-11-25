# stocks/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import StockDataProcessor
from .models import Stock
import pandas as pd

from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from accounts.models import UserProfile
from django.db import models  # models 임포트 추가


@api_view(['GET'])
def stock_list(request):
    try:
        # DB에서 데이터 조회
        stocks_data = list(Stock.objects.all().values())
        
        return Response({
            'count': len(stocks_data),
            'data': stocks_data
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'POST'])
def stock_update(request):
    try:
        # 데이터 처리 및 DB 저장
        stocks_df = StockDataProcessor.process_stock_data()
        
        Stock.objects.all().delete()
        
        stock_objects = [
            Stock(
                stock_id=row['종목코드'],
                stock_name=row['종목명'],
                current_price=int(str(row['종가']).replace(',', '')) if pd.notna(row['종가']) else None,
                price_change=row['등락'],
                price_change_rate=row['등락율'],
                volume=row['거래량'],
                trading_value=row['거래대금'],
                market_cap=row['시가총액'],
                issued_shares=row['발행주식수'],
                week_change_rate=row['1주간'],
                month_change_rate=row['1개월간'],
                year_change_rate=row['1년간'],
                three_year_change_rate=row['3년간'],
                beta=row['베타'],
                debt_ratio=row['부채비율'],
                retention_ratio=row['유보율'],
                revenue_growth_rate=row['매출액증가율'],
                eps_growth_rate=str(row['EPS증가율']),
                roa=row['ROA'],
                roe=row['ROE'],
                eps=row['EPS'],
                bps=row['BPS'],
                per=row['PER'],
                pbr=row['PBR'],
                ev_ebitda=row['EV/EBITDA'],
                revenue=str(row['매출액']) if pd.notna(row['매출액']) else None,
                evebitda=row['EVEBITDA'],
                sector=row['업종'],
                sector_per=row['업종평균PER']
            ) for _, row in stocks_df.iterrows()
            if pd.notna(row['종목코드'])
        ]
        
        Stock.objects.bulk_create(stock_objects)
        
        return Response({'message': 'Stock data updated successfully'}, 
                      status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    




@api_view(['GET'])
@permission_classes([IsAuthenticated])  # 인증된 사용자만 접근 가능
def get_stock_recommendations(request):
    try:
        # 현재 요청한 사용자의 프로필 가져오기
        user_profile = request.user.profile  # UserProfile 모델에서 OneToOne 관계로 연결되어 있다고 가정
        investment_style = user_profile.investment_style.style_id

        # 모든 주식 데이터 가져오기
        stocks = Stock.objects.all()
        total_stocks = stocks.count()

        # 투자 성향에 따라 추천 주식 필터링
        if investment_style == 'conservative':
            recommended_stocks = conservative_recommendations(stocks, total_stocks)
        elif investment_style == 'moderate':
            recommended_stocks = moderate_recommendations(stocks, total_stocks)
        else:  # aggressive
            recommended_stocks = aggressive_recommendations(stocks)

        return Response({
            'recommended_stocks': recommended_stocks[:10]  # 상위 10개만 반환
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def conservative_recommendations(stocks, total_stocks):
    # 시가총액 상위 20% 대형주 필터링
    large_caps = stocks.order_by('-market_cap')[:int(total_stocks * 0.2)]
    
    filtered_stocks = large_caps.filter(
        beta__lt=0.9,                          # 베타가 0.9 미만
        debt_ratio__lt=100,                   # 부채비율이 100% 미만
        per__lt=models.F('sector_per'),       # PER이 업종 평균 PER보다 낮음
        pbr__lte=1,                            # PBR이 1 이하
        roe__gt=10                             # ROE가 10% 이상
    )
    
    return list(filtered_stocks.order_by('-year_change_rate', '-three_year_change_rate').values())

def moderate_recommendations(stocks, total_stocks):
    # 시가총액 상위 20-60% 중형주 필터링
    mid_caps = stocks.order_by('-market_cap')[int(total_stocks * 0.2):int(total_stocks * 0.6)]
    
    filtered_stocks = mid_caps.filter(
        per__lt=models.F('sector_per'),       # PER이 업종 평균 PER보다 낮음
        roe__gte=10,                           # ROE가 10% 이상
        beta__range=(0.8, 1.2),               # 베타가 0.8에서 1.2 사이인 주식
        pbr__range=(1, 2)                     # PBR이 1에서 2 사이인 주식
    )
    
    return list(filtered_stocks.order_by('-roe').values())

def aggressive_recommendations(stocks):
    # 베타가 1.2 이상인 공격형 주식 필터링
    filtered_stocks = stocks.filter(
        beta__gt=1.2,                         # 베타가 1.2 이상
        per__lt=models.F('sector_per'),      # PER이 업종 평균 PER보다 낮음
        price_change_rate__gt=0               # 등락률이 양수인 주식
    )
    
    return list(filtered_stocks.order_by('-volume').values())