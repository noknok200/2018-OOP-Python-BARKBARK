"""
실행 안되면 안되는 대로 놔둬
"""
from __future__ import print_function
import sys
import matplotanimate_LES

def press(self):
    if matplotanimate_LES.first_click == 0:
        matplotanimate_LES.first_click = 1
    else:
        matplotanimate_LES.first_click = 0
        matplotanimate_LES.data_storage.append([matplotanimate_LES.click_time, matplotanimate_LES.t_time+100])
    click_time = matplotanimate_LES.t_time + 100
    matplotanimate_LES.click_time = click_time
    sys.stdout.flush()

matplotanimate_LES.fig.canvas.mpl_connect('button_press_event', press)
matplotanimate_LES.plt.show()