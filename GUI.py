import tkinter

def hamsoo():
    print("함수 호출이 됨.")

def screen():
    window = tkinter.Tk()
    window.title("Game_Table") #Table
    window.geometry("1285x673+100+10") #size
    window.resizable(False, False)

    tempo_button = tkinter.Button(window, text="함수 호출", height=10, width=33, command=hamsoo)
    tempo_button.grid(row=1, column=2)
    window.mainloop()

screen()