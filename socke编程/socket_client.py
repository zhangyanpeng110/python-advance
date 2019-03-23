# Author: O98K

import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
while True:
    input_data = input("输入回复的消息>>>\n")

    client.send(input_data.encode("utf8"))
    recive_data = client.recv(1024)
    print(recive_data.decode("utf8"))


