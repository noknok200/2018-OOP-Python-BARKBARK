from marcap.marcap_utils import marcap_date_range
from matplotlib import pyplot as plot
from matplotlib import animation
import matplotlib.dates as md
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd


def loader():
    code = '005930'
    stock = marcap_date_range('2015-01-01', '2015-12-31', code)['Close']
    empty = pd.Series([stock[0] for _ in range(100)])
    return 2015, empty.append(stock, ignore_index=True)


def plotter(y, stock_list):
    fig = plot.figure()
    ax = fig.add_subplot(1, 1, 1)

    dates_init = datetime.datetime(2015, 1, 1)
    datelist = []

    for i in range(len(stock_list)):
        d = relativedelta(day=i)
        datelist.append(dates_init + d)

    fmt = md.DateFormatter("%m")
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(fmt)
    fig.autofmt_xdate()

    # print(datelist)

    def animate(i):
        if i < len(stock_list) - 100:
            ax.clear()
            ax.plot(datelist[i:i+100], stock_list[i:i+100])

    ani = animation.FuncAnimation(fig, animate, interval=100)
    plot.show()


if __name__ == "__main__":
    year, stock_list = loader()
    plotter(year, stock_list)
