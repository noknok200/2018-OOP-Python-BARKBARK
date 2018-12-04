from marcap.marcap_utils import marcap_date
from marcap.marcap_utils import marcap_date_range
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np

from calculate_asset import cal_asset

# 삼성전자(005930), 시가총액 비중의 변화

#df_stock['MarcapRatio'].plot(figsize=(16, 6))

stock_data = []

'''외양 설정'''
mpl.rcParams['toolbar'] = 'None'
plt.style.use(['ggplot'])
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

ax1.get_xaxis().set_visible(False)
plt.grid(True, linestyle='--')
plt.get_current_fig_manager().full_screen_toggle()

'''구매가 및 판매가'''
price_buy = 0
price_sell = 0
state = '매수대기'  # 초기 매수대기
asset = 1e8  # 초기 자본
click_time = 0
first_click = 0
data_storage = [[0, 0]]
d_asset = 0

def new_point(old, pre, now):
    return (pre-old)*(stock_data[now]-stock_data[old])/(now-old)+stock_data[old]


def selecter(data1, data2):
    if stock_data[data2] - stock_data[data1] > 0:
        color_select = 'green'
    elif stock_data[data2] - stock_data[data1] == 0:
        color_select = 'white'
    else:
        color_select = 'red'
    return color_select


def animate(t):
    global click_time, first_click
    global t_time
    t_time = t
    points = np.ones(100)
    global state
    global state, price_buy, price_sell, asset
    global d_asset


    if t < len(stock_data) - 100:
        ax1.clear()
        ax1.plot(stock_data[t:t + 100])


        #현황 출력
        plt.title(str(asset), loc='left')
        plt.title(str(round(d_asset*100,2)), loc='right')
        
        color_select = selecter(click_time, t+100)

        #매도시 자산 계산
        if first_click ==0 and click_time !=0 and t+99<=click_time:
            price_sell = stock_data[t+99]
            prev_asset=asset
            
            
            #현황 출력
            prev_asset=asset
            asset=cal_asset(asset,price_buy,price_sell)
            d_asset=(asset-prev_asset)/asset
            print(str(asset)+' '+str(d_asset*100))

        #매수시 구매가격 저장
        elif first_click==1 and click_time !=0 and t+99<=click_time:
            price_buy = stock_data[t+99]

        #클릭포인트가 화면 안에 있을 때
        if first_click == 1 and click_time != 0 and t <= click_time:
            ax1.plot([click_time, t+100], [stock_data[click_time], stock_data[t+100]],
                     color=color_select)

        #클릭포인트가 화면밖으로 사라지면
        elif first_click == 1 and click_time != 0 and t > click_time:
            new_time = new_point(click_time, t, t+100)
            ax1.plot([t, t+100], [new_time, stock_data[t+100]],
                     color=color_select)
            price_sell = stock_data[t+100]

        # 저장되어 있는 data 그래프에 표현
        for storage in data_storage:
            if storage[1] > t:
                color_select = selecter(storage[0], storage[1])
                if t > storage[0]:
                    past_time = new_point(storage[0], t, storage[1])
                    ax1.plot([t, storage[1]], [past_time,
                                               stock_data[storage[1]]], color=color_select)
                else:
                    ax1.plot([storage[0], storage[1]], [
                        stock_data[storage[0]], stock_data[storage[1]]], color=color_select)

    else: #when the game is end,
        if first_click==1 :
            asset=cal_asset(asset,price_buy,price_sell)
            d_asset=(asset-1e8)/asset
            print(str(asset)+' '+str(d_asset*100))
        else :
            d_asset=(asset-1e8)/asset
            print(str(asset)+' '+str(d_asset*100))
        plt.pause(100000)
# for _ in len(player_list) :
    #     ax1.plot(range(i,i+100),player_list[_][0],)


def show():
    ani = animation.FuncAnimation(fig, animate, interval=100)
    plt.show()


def load():
    global stock_data
    code = '005930'
    df_stock = marcap_date_range('2017-01-01', '2018-12-31', code)
    df_stock = df_stock[df_stock['Code'] == '005930'].copy()
    latest_stocks = df_stock.iloc[-1]['Stocks']  # 범위 마지막날 주식수(기준)
    '''
    수정종가 코드
    '''
    df_stock['Adj Close'] = df_stock['Close'] * \
        (df_stock['Stocks'] / latest_stocks)  # 수정종가

    stock_data = df_stock['Adj Close']
