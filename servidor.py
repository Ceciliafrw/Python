from fileinput import close
import socket
import threading

TCP_ip = "127.0.0.1"
TCP_porta = 5002

servidor_TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_TCP.bind((TCP_ip, TCP_porta))
servidor_TCP.listen(5002)

print('Escutando %s:%d'%(TCP_ip, TCP_porta))

def recebendo_cliente(cliente_socket):
    request = cliente_socket.recv(1024)
    print('Reebido %s' %request)
    print('-----------------------------')
    cliente_socket.send(b'Mensagem recebida')
    cliente_socket.close()

while True:
    client, addr = servidor_TCP.accept()
    print('[*] Conexao aceita de: %s:%d' %(addr[0], addr[1]))
    client_handler = threading.Thread(target=recebendo_cliente, args=(client,))
    client_handler.start()
