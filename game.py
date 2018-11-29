from marcap.marcap_utils import marcap_date
from marcap.marcap_utils import marcap_date_range
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np

from calculate_asset import cal_asset
import keypress

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
# 삼성전자(005930), 시가총액 비중의 변화
code = '005930'
#df_stock['MarcapRatio'].plot(figsize=(16, 6))
df_stock = marcap_date_range('2016-01-01', '2018-12-31', code)

points = np.ones(100)

'''
수정종가 코드
'''
df_stock = df_stock[df_stock['Code'] == '005930'].copy()
latest_stocks = df_stock.iloc[-1]['Stocks']  # 범위 마지막날 주식수(기준)

df_stock['Adj Close'] = df_stock['Close'] * \
    (df_stock['Stocks'] / latest_stocks)  # 수정종가

stock_data = df_stock['Adj Close']


'''구매가 및 판매가'''
price_buy = 0
price_sell = 0
state = '매수대기' #초기 매수대기
asset = 1e8 #초기 자본


def animate(t):
    global state
    global price_buy
    global price_sell
    global asset
    
    ax1.clear()
    ax1.plot(stock_data[t:t+100])
    ax1.plot(range(t,t+100),stock_data[t+100]*points,color='red') #가장 마지막 가격을 선으로 나타냄
    
    '''
    player가 구매한 경우 
    '''
    if state == '매수대기' :
        if keypress.key_pressed() :
            price_buy = stock_data[t+100] #현재가로 매수
            state = '매도대기' #매도대기 상태로 변경
            print(state)

    elif state == '매도대기' :
        if keypress.key_pressed() :
            price_sell=stock_data[t+100] #매도 대기중에 버튼을 누르면 현재가로 매도
            asset = cal_asset(asset, price_buy, price_sell) #자본 계산
            state = '매수대기' #매수대기 상태로 변경
            print(state)
            print(asset)

        ax1.plot(range(t,t+100),price_buy*points,color='blue') #매도대기 상태에서는 현재 얼마에 매수하였는지 표시

    # for _ in len(player_list) :
    #     ax1.plot(range(i,i+100),player_list[_][0],)
    
ani = animation.FuncAnimation(fig, animate, interval=100)

plt.show()
