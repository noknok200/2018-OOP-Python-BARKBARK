'''
이거 실행시켜서 게임시작!
'''
# The main module to be executed

from plot_keybind import startstock
from plot_core import initcore
from time import sleep

while True:
    initcore()
    sleep(1)
    startstock()
