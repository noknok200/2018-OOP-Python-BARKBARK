import datetime
import tkinter
import queue

mytempo = 0
que = queue.Queue(4)

def page1_tempo():
    global mytempo
    current_time = datetime.datetime.now()
    current_time = str(current_time).split()[1].split(':')
    minute = int(current_time[1])
    second = float(current_time[2])
    time_for_tempo = minute * 60 + second

    if que.qsize() < 3:
        que.put(time_for_tempo)
    else:
        mytempo = int(60 * 4 / (time_for_tempo - que.get()))
        que.put(time_for_tempo)

    catch_tempo.configure(text=mytempo)


def page1():
    tempo_button = tkinter.Button(window, text="tempo", height=10, width=33, command=page1_tempo)
    tempo_button.grid(row=1, column=2)
    window.mainloop()

window = tkinter.Tk()
window.title("Time_Table")
window.geometry("1285x673+100+10")
window.resizable(False, False)

catch_tempo = tkinter.Button(window, text=mytempo, height=10, width=33)
catch_tempo.grid(row=2, column=3)
page1()