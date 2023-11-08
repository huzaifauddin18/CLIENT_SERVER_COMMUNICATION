import socket
host = '192.168.29.5'
port = 8080
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))
socket.send(f"Hai how are you".encode('UTF-8'))
socket.send(f"had your lunch".encode('UTF-8'))



print(socket.recv(1028).decode('UTF-8'))

#cd PycharmProjects cd pythonProject2 python server.py python client.py
