# stock/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import StockDataProcessor

class StockListView(APIView):
    def get(self, request):
        try:
            # 데이터 처리
            stocks_df = StockDataProcessor.process_stock_data()
            
            # 필터링 파라미터
            sector = request.query_params.get('sector')
            min_trading_value = request.query_params.get('min_trading_value')
            
            # 필터링 적용
            if sector:
                stocks_df = stocks_df[stocks_df['업종'] == sector]
            if min_trading_value:
                stocks_df = stocks_df[stocks_df['거래대금'] >= float(min_trading_value)]
            
            # DataFrame을 딕셔너리 리스트로 변환
            stocks_data = stocks_df.to_dict('records')
            
            return Response({
                'count': len(stocks_data),
                'data': stocks_data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)