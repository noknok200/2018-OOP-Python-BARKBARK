import plot_keybind as pk
import plot_core as pc
import threading

stockdat = []


def showstock():
    global stockdat
    if len(stockdat) == 0:
        pc.load()

    loader = threading.Thread(target=pc.load)
    shower = threading.Thread(target=pk.startstock, args=stockdat)

    loader.start()
    shower.start()

    loader.join()
    shower.join()
