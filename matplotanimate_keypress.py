"""
실행 안되면 안되는 대로 놔둬

"""
from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt
import game

def press():
    print("성공")
    sys.stdout.flush()

game.fig.canvas.mpl_connect('key_press_event', press)
game.plt.show()