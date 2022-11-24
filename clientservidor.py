from ast import While
from distutils.spawn import spawn
import socket

TCP_ip = "localhost"
TCP_porta = 5002

msg = input("Qual sua mensagem? ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_ip, TCP_porta))
s.sendall(str.encode(msg))
data = s.recv(1024)

print('Conectado: ', data.decode())
