"""
실행 안되면 안되는 대로 놔둬
"""
from __future__ import print_function
import sys
from marcap import matplotanimate_LES

def press(self):
    click_time = matplotanimate_LES.t_time+100
    matplotanimate_LES.click_time = click_time
    sys.stdout.flush()

matplotanimate_LES.fig.canvas.mpl_connect('key_press_event', press)
matplotanimate_LES.plt.show()