from marcap.marcap_utils import marcap_date
from marcap.marcap_utils import marcap_date_range
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np

fig=plt.figure()
ax1=fig.add_subplot(1,1,1) 
# 삼성전자(005930), 시가총액 비중의 변화
code = '005930'
df_stock = marcap_date_range('2016-01-01', '2018-12-31', code)


points=np.ones(100)

'''
수정종가 코드
'''
df_stock = df_stock[df_stock['Code'] == '005930'].copy()
latest_stocks = df_stock.iloc[-1]['Stocks'] # 범위 마지막날 주식수(기준)

df_stock['Adj Close'] = df_stock['Close'] * (df_stock['Stocks'] / latest_stocks) # 수정종가

def animate(i):
    ax1.clear()
    ax1.plot(df_stock['Adj Close'][i:i+100])
    ax1.plot(range(i,i+100),df_stock['Adj Close'][i+100]*points,color='red') #가장 마지막 가격을 선으로 나타냄

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
