# client 들의 위치 데이터를 받으면서 game.py를 실행하는 함수, 이 파일이 메인이 될 예정
# 데이터 처리 법
'''
받는 값
(누르거나 뗀 시점, 총 점수)

보내는 값
(클라이언트 ip, 누르거나 뗀 시점, 총점수)
-누르지 않은 경우
(클라이언트 ip, 0 , 총점수)
'''
import socket
import threading
import matplotanimate_keypress

myip = ''
myport = 50000
address = (myip, myport)

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()

# 접속한 클라이언트들을 저장할 공간
client_list = []
client_id = []

# 서버로 부터 메시지를 받는 함수 | Thread 활용


def receive(client_sock):
    global client_list  # 받은 메시지를 다른 클라이언트들에게 전송하고자 변수를 가져온다.
    while True:
        # 클라이언트로부터 데이터를 받는다.
        try:
            data = client_sock.recv(1024)
            connect = data.decode('UTF-8')
            imfo = connect.split(".")
            matplotanimate_keypress.matplotanimate_LES.opposcore.plotter(client_sock,imfo[0],imfo[1],imfo[2])
        except ConnectionError:
            print("{}와 연결이 끊겼습니다. #code1".format(client_sock.fileno()))
            break
        # 만약 클라이언트로부터 종료 요청이 온다면, 종료함. code0 : 클라이언트 전송 기능 닫았을때 오는 메시지
        if not data:
            print("{}이 연결 종료 요청을 합니다. #code0".format(client_sock.fileno()))
            client_sock.send(bytes("서버에서 클라이언트 정보를 삭제하는 중입니다.", 'utf-8'))
            break

        # 데이터가 들어왔다면 접속하고 있는 모든 클라이언트에게 메시지 전송
        for sock in client_list:
            if sock != client_sock:
                sock.send(bytes(data, 'UTF-8'))

    # 메시지 송발신이 끝났으므로, 대상인 client는 목록에서 삭제.
    client_id.remove(client_sock.fileno())
    client_list.remove(client_sock)
    print("현재 연결된 사용자: {}\n".format(client_id), end='')
    # 삭제 후 sock 닫기
    client_sock.close()
    print("클라이언트 소켓을 정상적으로 닫았습니다.")
    print('#----------------------------#')
    return 0

# 연결 수립용 함수 | Thread 활용


def connection():
    global client_list
    global client_id

    while True:
        # 클라이언트들이 접속하기를 기다렸다가, 연결을 수립함.
        client_sock, client_addr = server_sock.accept()

        # 연결된 정보를 가져와서 list에 저장함.
        client_list.append(client_sock)
        client_id.append(client_sock.fileno())

        print("{}가 접속하였습니다.".format(client_sock.fileno()))
        print("{}가 접속하였습니다.".format(client_addr))
        print("현재 연결된 사용자: {}\n".format(client_list))

        # 접속한 클라이언트를 기준으로 메시지를 수신 할 수 있는 스레드를 생성함.
        thread_recv = threading.Thread(target=receive, args=(client_sock,))
        thread_recv.start()


# 연결 수립용 스레드 생성 및 실행.
thread_server = threading.Thread(target=connection, args=())
thread_server.start()

matplotanimate_keypress.matplotanimate_LES.fig.canvas.mpl_connect('key_press_event', matplotanimate_keypress.press)
matplotanimate_keypress.matplotanimate_LES.plt.show()
# game_start()  # game start!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

thread_server.join()
server_sock.close()
