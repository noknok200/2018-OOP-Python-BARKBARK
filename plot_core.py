from marcap.marcap_utils import marcap_date
from marcap.marcap_utils import marcap_date_range
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np
import threading
from random import randrange
from calculate_asset import cal_asset

stock_data = [] #클릭을 통해 user가 매수 및 매도한 시점을 저장 - 차기에 멀티플레이에서 사용 가능

'''외양 설정'''
mpl.rcParams['toolbar'] = 'None'
plt.style.use(['ggplot'])

<<<<<<< HEAD

# plt.get_current_fig_manager().full_screen_toggle()
=======
ax1.get_xaxis().set_visible(False)
plt.grid(True, linestyle='--')
# plt.get_current_fig_manager().full_screen_toggle() 다음 line을 사용하면 전체화면으로 이용가능
>>>>>>> c2f7f59808e6a15555fd68a5bd2869c4a2b35b69

'''구매가 및 판매가'''
price_buy = 0
price_sell = 0
state = '매수대기'  # 초기 매수대기
asset = 1e8  # 초기 자본
d_asset = 0
t_time = 0

click_time = 0
first_click = 0
<<<<<<< HEAD
data_storage = []
=======
data_storage = [[0, 0]] #클릭 후 잔상을 남기기 위한 리스트
opponent_list = [[0, 0]] #다른 상대들의 기록을 다음 리스트로 볼 수 있음 - 멀티플레이 게임에 사용가능
>>>>>>> c2f7f59808e6a15555fd68a5bd2869c4a2b35b69
# [0, 0], [104, 176], [178, 183], [186, 189], [194, 224], [228, 234], [239, 358], [366, 374], [377, 381], [388, 395], [404, 409], [416, 435]
start_data1 = 0
start_data2 = 0
opponent_score = 0

fig = None
ax1 = None

isgoing = False


def initcore():
    global fig, ax1, stock_data, data_storage, click_time, first_click, start_data1, start_data2
    data_storage = [[0, 0]]
    start_data1 = 0
    start_data2 = 0
    first_click = 0
    click_time = 0

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    ax1.get_xaxis().set_visible(False)
    plt.grid(True, linestyle='--')


def new_point(old, pre, now): #기울기 계산 함수 함수값을 반환한다.
    return (pre-old)*(stock_data[now]-stock_data[old])/(now-old)+stock_data[old]


def selecter(data1, data2): #상한가, 하한가, 정가에 따라서 다양한 색을 결정해주는 함수
    if stock_data[data2] - stock_data[data1] > 0:
        color_select = 'red'
    elif stock_data[data2] - stock_data[data1] == 0:
        color_select = 'black'
    else:
        color_select = 'blue'
    return color_select


def clicking_plotter(now_left, now_right, left, right, color): #이미 매도가 끝난 시점들의 잔상을 남기거나 매수는 이미 했고 매도를 할 시점을 따라가주는 함수
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


def _animate(t): #그래프를 animate화 하여 움직이는 것 처럼 출력해주는 함수
    global click_time, first_click, t_time, state, price_buy, price_sell, asset, d_asset

    t_time = t

    if t < len(stock_data) - 100:
        ax1.clear()
        ax1.plot(stock_data[t:t + 100])
        plt.title('{}/{}'.format(t + 1, len(stock_data)-100), loc='center')

        # 현황 출력
        plt.title('asset: '+str(asset), loc='left')
        plt.title(str(round(d_asset*100, 2))+'%', loc='right')

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
            print(str(asset) + ' ' + str(d_asset * 100))

        plt.title('final asset:'+str(asset), loc='left')
        plt.title('final rate: ' +
                  str(round(d_asset * 100, 2)) + '%', loc='right')

        try:
            plt.pause(1000)
        except Exception:
            print('waiting for next one....')


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

    while isgoing:
        time.sleep(1)

    stock_data = df_stock['Adj Close']


def show():
    global stock_data, isgoing
    year = randrange(1995, 2018)

    if len(stock_data) == 0:
        print('no data loaded currently. loading.')
        _load(str(year) + '-01-01', str(year + 1) + '-12-31', '005930')
        year = randrange(1995, 2018)

    s = threading.Thread(target=_load, args=(
        str(year) + '-01-01', str(year + 1) + '-12-31', '005930'))
    s.start()

    isgoing = True

    ani = animation.FuncAnimation(fig, _animate, interval=100)
<<<<<<< HEAD
    plt.show()

    isgoing = False
=======
    plt.show()
>>>>>>> c2f7f59808e6a15555fd68a5bd2869c4a2b35b69
