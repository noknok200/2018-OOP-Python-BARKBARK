from marcap.marcap_utils import marcap_date
from marcap.marcap_utils import marcap_date_range
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np
import threading

from calculate_asset import cal_asset
from keypress_mac import listner

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
# 삼성전자(005930), 시가총액 비중의 변화
code = '005930'
#df_stock['MarcapRatio'].plot(figsize=(16, 6))
df_stock = marcap_date_range('2018-01-01', '2018-12-31', code)

points = np.ones(100)

'''
수정종가 코드
'''
df_stock = df_stock[df_stock['Code'] == '005930'].copy()
latest_stocks = df_stock.iloc[-1]['Stocks']  # 범위 마지막날 주식수(기준)

df_stock['Adj Close'] = df_stock['Close'] * \
    (df_stock['Stocks'] / latest_stocks)  # 수정종가

stock_data = df_stock['Adj Close']



class Game(threading.Thread):
    def __init__(self):
        '''구매가 및 판매가'''
        self.price_buy = 0
        self.price_sell = 0
        self.state = '매수대기' #초기 매수대기
        self.asset = 1e8 #초기 자본

    def animate(self,t):
        ax1.clear()
        ax1.plot(stock_data[t:t+100])
        ax1.plot(range(t,t+100),stock_data[t+100]*points,color='red') #가장 마지막 가격을 선으로 나타냄
        
        '''
        player가 구매한 경우 
        '''
        if state == '매수대기' :
            if listner() :
                price_buy = stock_data[t+100] #현재가로 매수
                state = '매도대기' #매도대기 상태로 변경
                print(state)

        elif state == '매도대기' :
            if listner() :
                price_sell=stock_data[t+100] #매도 대기중에 버튼을 누르면 현재가로 매도
                asset = cal_asset(asset, price_buy, price_sell) #자본 계산
                state = '매수대기' #매수대기 상태로 변경
                print(state)
                print(asset)

            ax1.plot(range(t,t+100),price_buy*points,color='blue') #매도대기 상태에서는 현재 얼마에 매수하였는지 표시

    # with keypress_mac.Listener
        # for _ in len(player_list) :
        #     ax1.plot(range(i,i+100),player_list[_][0],)
        
    ani = animation.FuncAnimation(fig, animate, interval=100)
    #display = threading.Thread(target = animation.FuncAnimation, args = (fig, animate), kwargs = {'interval' : 100})

    #display.start()
    plt.show()

Game()
