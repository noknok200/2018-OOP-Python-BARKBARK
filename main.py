import game
import multiplay

"""
모듈을 합치는 메인 파일.
이걸 실행시킨다.
"""

mode = input("1: 싱글플레이\n2: 멀티플레이")

if mode==1 :
    Game=game(1,args)
    score=Game.score()

    print("점수는 %d점 입니다".)
elif mode==2 :
    game(2,args)