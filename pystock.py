# The main module to be executed

import plot_keybind as pk
import threading
from time import sleep

stockdat = []


while True:
    pk.startstock()
    sleep(1)
