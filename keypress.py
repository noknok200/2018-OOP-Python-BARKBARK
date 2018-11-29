#그냥 부분적으로 코드를 넣어서 연습하는 py
#아무 의미 없다.

import threading
import keyboard
import tkinter

def key_pressed(self):  #self
    print("Click")
    return True

def main_thread():
    root = tkinter.Tk()
    root.bind_all('<Key>', key_pressed)
    root.withdraw()
    root.mainloop()

thread_main = threading.Thread(target=main_thread, args=())
thread_main.start()
