import random
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 1080))

while True:
    rand = random.randint(0, 10)
    message, address = server_socket.recvfrom(1024)
    print("addr:", address)
    print("message:", message)
    server_socket.sendto(message, address)
