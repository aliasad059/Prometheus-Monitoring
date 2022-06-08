import socket

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        Input = input('Hey there: ')
        s.sendall(str.encode(Input))
        res = s.recv(1024)
        print(res.decode('utf-8'))
        if Input == 'exit':
            break