# stocks/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .utils import StockDataProcessor
from .models import Stock
import pandas as pd

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

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def stock_like(request, stock_id):
    stock = get_object_or_404(Stock, stock_id=stock_id)
    
    if stock.likes.filter(pk=request.user.pk).exists():
        stock.likes.remove(request.user)
        is_liked = False
    else:
        stock.likes.add(request.user)
        is_liked = True
    
    return Response({
        'is_liked': is_liked,
        'like_count': stock.likes.count()
    })