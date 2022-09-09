import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 7777
MESSAGE = b'{"iv": "JiHc9vDfMzIyiPa6esl8gw==", "ct": "gUIF98uXKN/eZGj7VLolUzrsR/wHyNva5EIUT5+WTq9h", "aluno": "Cecilia"}'


#print("UDP target IP: %s" % UDP_IP)
#print("UDP target port: %s" % UDP_PORT)
#print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, 
socket.SOCK_DGRAM, socket.IPPROTO_UDP)

sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
