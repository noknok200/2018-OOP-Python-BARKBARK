"""
점수 계산 파일.
처음 가격과 나중 가격의 차이를 반영하여 계산.
"""

def cal_asset(asset, price_buy, price_sell) :
    number_of_stocks=int(asset/price_buy) #구매가로 전액 매수한 주식 수량
    asset_after=asset-number_of_stocks*price_buy #최대 매수 후 남은 잔고
    asset_after=asset_after+number_of_stocks*price_sell #현재 매도가로 전량 매도
    return asset_after