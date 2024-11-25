# stock/utils.py
import pandas as pd
import FinanceDataReader as fdr
import os
from django.conf import settings

BASE_PATH = os.path.join(settings.BASE_DIR, 'stocks', 'data')
class StockDataProcessor:
    @staticmethod
    def process_stock_data():
    
        # 1. FnGuide 데이터 처리
        fnguide_kospi = pd.read_csv(f'{BASE_PATH}/stock_kospi.csv', encoding='cp949')
        fnguide_kosdaq = pd.read_csv(f'{BASE_PATH}/stock_kosdaq.csv', encoding='cp949')
        fnguide = pd.concat([fnguide_kospi, fnguide_kosdaq], axis=0)

        # 2. Investing.com 데이터 처리
        accom = pd.concat([
            pd.read_csv(f'{BASE_PATH}/성과_kospi.csv'),
            pd.read_csv(f'{BASE_PATH}/성과_kosdaq.csv')
        ], axis=0)

        funda = pd.concat([
            pd.read_csv(f'{BASE_PATH}/펀더멘탈_kospi.csv'),
            pd.read_csv(f'{BASE_PATH}/펀더멘탈_kosdaq.csv')
        ], axis=0)

        investing = pd.merge(accom, funda, on='종목명')
        investing = investing.drop(['YTD', '평균 거래량', '매출', '주가수익비율'], axis=1)
        investing = investing.drop_duplicates('종목명')

        # 3. FnGuide + Investing.com
        fnin = pd.merge(investing, fnguide, on='종목명')

        # 4. KRX 데이터
        krx = fdr.StockListing('KRX')
        krx = krx[(krx['Market']=='KOSPI')|(krx['Market']=='KOSDAQ')]
        krx = krx.rename(columns={'Name':'종목명'})

        # 최종 데이터 병합
        result = pd.merge(krx, fnin, on='종목명')

        # 데이터 전처리
        result.loc[result['부채비율'] == '완전잠식', '부채비율'] = 9999.0
        result.loc[result['ROE'] == '완전잠식', 'ROE'] = -9999.0
        result['부채비율'] = result['부채비율'].apply(lambda x: float(x))
        result['ROE'] = result['ROE'].apply(lambda x: float(x))

        # 업종 정보 추가
        code_industry = pd.read_csv(f'{BASE_PATH}/finance_data_batch.csv', encoding='cp949')
        code_industry['종목코드'] = code_industry['종목코드'].apply(lambda x: str(x).zfill(6))
        stocks = pd.merge(result, code_industry, left_on='Code', right_on='종목코드', how='left')

        # 최종 컬럼 정리
        stocks = stocks.drop(['일간', '총 시가', '시장', 'ISU_CD', '종목코드', 'Market', 'Dept', 
                            'ChangeCode', 'MarketId', 'Open', 'High', 'Low'], axis=1)
        stocks = stocks.drop_duplicates('Code')
        
        # 컬럼명 변경
        stocks.columns = ['종목코드', '종목명', '종가', '등락', '등락율', '거래량', '거래대금', 
                         '시가총액', '발행주식수', '1주간', '1개월간', '1년간', '3년간', 
                         '베타', '부채비율', '유보율', '매출액증가율', 'EPS증가율', 'ROA', 
                         'ROE', 'EPS', 'BPS', 'PER', 'PBR', 'EV/EBITDA', '매출액', 
                         'EVEBITDA', '업종']

        # 필터링
        stocks = stocks[stocks['거래대금'] > 0]
        stocks = stocks[~stocks['종목명'].str.contains('스팩')]
        stocks = stocks.reset_index()

        # 업종별 PER 평균 계산
        mean_table = stocks.groupby('업종')['PER'].mean()
        stocks['업종평균PER'] = stocks['업종'].map(mean_table)
        
        stocks = stocks.fillna('Nan')
        return stocks
