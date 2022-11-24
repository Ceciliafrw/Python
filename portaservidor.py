from ast import While
from distutils.spawn import spawn
import socket

TCP_ip = "localhost"
TCP_porta = 5002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_ip, TCP_porta))
s.listen()
print('Aguardando conexão')
conn, ender = s.accept()

print('Conectado em', ender)

while True:
    data = conn.recv(1024)
    if not data:
        print('Fechando a conexão')
        conn.close()
        break
    conn.sendall(data)
