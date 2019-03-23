# Author: O98K

import socket
import threading
import gevent

# 指定 IP协议 和 传输层协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定IP 和 端口
server.bind(('0.0.0.0', 8000))
# 开启监听
server.listen()


def socket_threding(sock, addr):
    while True:
        recive_data = sock.recv(1024)
        print(recive_data.decode('utf-8'))
        input_data = input("输入回复的消息>>>\n")
        sock.send(input_data.encode('utf-8'))

# 获取从客户端发送过来的数据 指定每次接收的数据量
while True:
    # 获取连接对象 和 IP address
    sock, addr = server.accept()

    # 使用线程接收请求
    client_thread = threading.Thread(target=socket_threding, args=(sock, addr))
    client_thread.start()

    # recive_data = sock.recv(1024)
    # print(recive_data.decode('utf-8'))
    # input_data = input("输入回复的消息>>>")
    # sock.send(input_data.encode('utf-8'))
    #
    # # 关闭服务连接
    # server.close()
    # sock.close()

