# server에 데이터를  주고 받으면서 plot_core.py를 실행하는 함수, 이 파일이 메인이 될 예정
# 데이터 처리 법
'''
my_place
(누르거나 뗀 시점, 총 점수)

받는 값
(클라이언트 ip. 누르거나 뗀 시점, 총 점수)

주식데이터날짜=날짜/점수/좌표,좌표.좌표,좌표............
'''

import socket
import threading
import plot_core

# 접속할 서버의 정보
server_ip = '127.0.0.1'
server_port = 50000
address = (server_ip, server_port)

# 소켓을 이용해서 서버에 접속
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(address)
print("connection complete")


# 서버로부터 메시지를 받아, 출력하는 함수.
def receive():
    global mysock
    while True:
        try:
            data = mysock.recv(1024)  # 서버로 부터 값을 받는것
            temp = data.decode('UTF-8')
            opponent_imfo = temp.split("/")

            if opponent_imfo != [""]:
                our_game_date = opponent_imfo[0].split("=")
                plot_core.start_data1, plot_core.start_data2 = our_game_date[0], our_game_date[1]
                plot_core.opponent_score = opponent_imfo[1]
                preopponent_list = opponent_imfo[2].split(".")
                opponent_list = []

                for i in preopponent_list:
                    start_end = i.split(",")
                    opponent_list.append([start_end[0], start_end[1]])
                plot_core.opponent_list = opponent_list
                # plot_core._graph() #plot_core함수가 제대로 돌아가지 않고 있음
                print(plot_core.opponent_list)

        except ConnectionError:
            print("서버와 접속이 끊겼습니다. Enter를 누르세요.")
            break

        if not data:  # 넘어온 데이터가 없다면.. 로그아웃!
            print("서버로부터 정상적으로 로그아웃했습니다.")
            break

    print('소켓의 읽기 버퍼를 닫습니다.')
    mysock.shutdown(socket.SHUT_RD)


# 메시지 받는 스레스 시작
thread_recv = threading.Thread(target=receive, args=())
thread_recv.start()

# # 메시지 보내는 스레드 시작
# thread_main = threading.Thread(target=main_thread, args=())
# thread_main.start()

# 메시지를 받고, 보내는 스레드가 종료되길 기다림
# thread_main.join()
thread_recv.join()

# 스레드가 종료되면, 열어둔 소켓을 닫는다.
mysock.close()
print('소켓을 닫습니다.')
print('클라이언트 프로그램이 정상적으로 종료되었습니다.')
