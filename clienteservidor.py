from http import client
import socket

TCP_ip = "127.0.0.1"
TCP_porta = 5002

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((TCP_ip,TCP_porta))
client.send(b'Cecilia conseguiu criar um servidor')

response = client.recv(4096)
print(response)