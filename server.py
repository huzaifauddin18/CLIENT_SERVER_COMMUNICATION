import socket
host = socket.gethostbyname(socket.gethostname())
port = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen(10)
while True:
    communication_socket, address = server.accept()
    print(f'communication with {address} has started')
    message = communication_socket.recv(1028).decode('UTF-8')
    print(f'The clients message is : {message}')
    communication_socket.send("Hai got your request ".encode('UTF-8'))
    communication_socket.close()
    print(f'The communication with {address} has ended')

