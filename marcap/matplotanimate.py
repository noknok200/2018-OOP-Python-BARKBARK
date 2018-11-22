
from marcap_utils import marcap_date
from marcap_utils import marcap_date_range
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# plt.title("Plot")
# plt.plot([1, 4, 9, 16])
# plt.show()

# df = marcap_date_range('2017-01-01', '2018-10-31')

# print('row count:', len(df))
# df.head()

fig=plt.figure()
ax1=fig.add_subplot(1,1,1) 
# 삼성전자(005930), 시가총액 비중의 변화
code = '005930'
df_stock = marcap_date_range('2015-01-01', '2018-12-31', code)
#df_stock['MarcapRatio'].plot(figsize=(16, 6))

def animate(i):
    ax1.clear()
    ax1.plot(df_stock['Close'][i:i+100])

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()