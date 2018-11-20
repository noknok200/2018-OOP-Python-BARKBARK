import tkinter

def hamsoo(self): #self라고 적는 것이 필수적
    print("함수 호출이 됨.")

def screen():
    window = tkinter.Tk()
    window.title("Game_Table") #Table
    window.geometry("1285x673+100+10") #size
    window.resizable(False, False)

    tempo_button = tkinter.Button(window, text="key를 눌러 함수 호출", height=10, width=33) #그냥 버튼 생성, 눌러도 실행 안됨.
    tempo_button.grid(row=1, column=2)

    window.bind("<Key>", func=hamsoo) #<Key>는 키보드를 눌렀을 때라는 의미, func=hamsoo 호출을 window창에 묶기.

    window.mainloop()

screen()