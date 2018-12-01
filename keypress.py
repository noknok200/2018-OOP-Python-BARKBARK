import threading
import keyboard
import tkinter
from pynput.keyboard import Key, Listener

def key_pressed(key):  #self
    print("Click")
    return True

def main_thread():
    root = tkinter.Tk()
    root.bind_all('<Key>', key_pressed)
    root.withdraw()
    root.mainloop()

thread_main = threading.Thread(target=main_thread, args=())
thread_main.start()