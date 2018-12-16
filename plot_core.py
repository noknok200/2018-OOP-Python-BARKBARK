from marcap.marcap_utils import marcap_date
from marcap.marcap_utils import marcap_date_range
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np
import threading

from calculate_asset import cal_asset

stock_data = []

'''외양 설정'''
mpl.rcParams['toolbar'] = 'None'
plt.style.use(['dark_background'])
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

ax1.get_xaxis().set_visible(False)
plt.grid(True, linestyle='--')
# plt.get_current_fig_manager().full_screen_toggle()

'''구매가 및 판매가'''
price_buy = 0
price_sell = 0
state = '매수대기'  # 초기 매수대기
asset = 1e8  # 초기 자본
t_time = 0

click_time = 0
first_click = 0
data_storage = [[0, 0]]
# [0, 0], [104, 176], [178, 183], [186, 189], [194, 224], [228, 234], [239, 358], [366, 374], [377, 381], [388, 395], [404, 409], [416, 435]
opponent_list = [[0, 0]]
start_data1 = 0
start_data2 = 0
opponent_score = 0


def new_point(old, pre, now):
    return (pre-old)*(stock_data[now]-stock_data[old])/(now-old)+stock_data[old]


def selecter(data1, data2):
    if stock_data[data2] - stock_data[data1] > 0:
        color_select = 'red'
    elif stock_data[data2] - stock_data[data1] == 0:
        color_select = 'black'
    else:
        color_select = 'blue'
    return color_select


def clicking_plotter(now_left, now_right, left, right, color):
    if right <= now_right:
        if now_left <= left:
            ax1.plot([left, right], [stock_data[left],
                                     stock_data[right]], color=color)
        else:
            new_leftvalue = new_point(left, now_left, right)
            ax1.plot([now_left, right], [new_leftvalue,
                                         stock_data[right]], color=color)
    else:
        new_rightvalue = new_point(left, now_right, right)
        if now_left <= left:
            ax1.plot([left, now_right], [
                     stock_data[left], new_rightvalue], color=color)
        else:
            new_leftvalue = new_point(left, now_left, right)
            ax1.plot([now_left, now_right], [
                     new_leftvalue, new_rightvalue], color=color)


def _animate(t):
    global click_time, first_click, t_time, state, price_buy, price_sell, asset

    if t < len(stock_data) - 100:
        ax1.clear()
        ax1.plot(stock_data[t:t + 100])

        # ax1.plot(range(t,t+100),stock_data[t+100]*points,color='red') #가장 마지막 가격을 선으로 나타냄
        '''
        player가 구매한 경우
        '''
        # if state == '매수대기' :
        #     if keypress.key_pressed() :
        #         price_buy = stock_data[t+100] #현재가로 매수
        #         state = '매도대기' #매도대기 상태로 변경
        #         print(state)
        #
        # elif state == '매도대기' :
        #     if keypress.key_pressed() :
        #         price_sell=stock_data[t+100] #매도 대기중에 버튼을 누르면 현재가로 매도
        #         asset = cal_asset(asset, price_buy, price_sell) #자본 계산
        #         state = '매수대기' #매수대기 상태로 변경
        #         print(state)
        #         print(asset)
        # ax1.plot(range(t, t + 100), price_buy * points, color='blue')  # 매도대기 상태에서는 현재 얼마에 매수하였는지 표시

        # 현황 출력
        plt.title(str(asset), loc='left')
        # plt.title(str(round(d_asset*100, 2)), loc='right')

        # 매도시 자산 계산
        if first_click == 0 and click_time != 0 and t+99 <= click_time:
            price_sell = stock_data[t+99]
            prev_asset = asset

            # 현황 출력
            prev_asset = asset
            asset = cal_asset(asset, price_buy, price_sell)
            d_asset = (asset-prev_asset)/asset
            print(str(asset)+' '+str(d_asset*100))

        # 매수시 구매가격 저장
        elif first_click == 1 and click_time != 0 and t+99 <= click_time:
            price_buy = stock_data[t+99]

        if first_click == 1 and click_time != 0:
            color_select = selecter(click_time, t+100)
            clicking_plotter(t, t+100, click_time, t+100, color_select)

        # 저장되어 있는 data 그래프에 표현
        for storage in data_storage:
            if storage[1] > t:
                color_select = selecter(storage[0], storage[1])
                clicking_plotter(
                    t, t+100, storage[0], storage[1], color_select)

        for opponent_imfo in opponent_list:
            if opponent_imfo[0] <= t+100 and opponent_imfo[1] >= t:
                clicking_plotter(
                    t, t+100, opponent_imfo[0], opponent_imfo[1], 'gray')

    else:  # when the game is end,
        if first_click == 1:
            asset = cal_asset(asset, price_buy, price_sell)
            d_asset = (asset-1e8)/asset
            print(str(asset)+' '+str(d_asset*100))
        else:
            d_asset = (asset-1e8)/asset
            print(str(asset)+' '+str(d_asset*100))
        plt.pause(100000)
# for _ in len(player_list) :
    #     ax1.plot(range(i,i+100),player_list[_][0],)


def _load(start_data1, start_data2, code):
    global stock_data

    # 함수실행할때 start_data에 값을 넣어줌
    df_stock = marcap_date_range(start_data1, start_data2, code)
    print('_load: loaded {} datas'.format(len(df_stock)))
    df_stock = df_stock[df_stock['Code'] == code].copy()
    latest_stocks = df_stock.iloc[-1]['Stocks']  # 범위 마지막날 주식수(기준)

    '''
    수정종가 코드
    '''
    df_stock['Adj Close'] = df_stock['Close'] * \
        (df_stock['Stocks'] / latest_stocks)  # 수정종가
    stock_data = df_stock['Adj Close']


def show():
    global stock_data
    if len(stock_data) == 0:
        print('no data loaded currently. loading.')
        _load('2017-01-01', '2017-12-31', '005930')
    s = threading.Thread(target=_load, args=(
        '2017-01-01', '2017-12-31', '005930'))
    s.start()

    ani = animation.FuncAnimation(fig, _animate, interval=100)
    plt.show()


# 이걸로 실행해 보기...실행이 안됨
# start_data1 = "2018-01-01"
# start_data2 = "2018-12-31"
# show()
# _graph()
