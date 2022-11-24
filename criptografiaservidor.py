from pydoc import text
from unittest import result
from Crypto.Cipher import AES
import json
from base64 import b64encode, b64decode

def criptografar(msgdata):
    #data = bytes("Cecília Linda!!", 'utf-8')
    msgdata = b'Boa noite...sera que consegui???"'
    key = b64decode('ABEiM0RVZneImQARIjNEVQ==')
    cipher = AES.new(key, AES.MODE_CFB)
    ct_raw = cipher.encrypt(msgdata)
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_raw).decode('utf-8')
    result = bytes(json.dumps({'iv':iv, 'ct':ct, 'aluno':'Cecilia'}), 'utf-8')

    print (result)
    return result, iv, ct

def descriptografar(mensagem):
    
    key = b64decode('ABEiM0RVZneImQARIjNEVQ==')
    cipher = AES.new(key, AES.MODE_CFB)
    ct_raw = cipher.encrypt(mensagem)
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_raw).decode('utf-8')
    result = bytes(json.dumps({'iv':iv, 'ct':ct, 'aluno':'Cecilia'}), 'utf-8')
    
    print (result)
    
    json_input=(f"''{result}''")
    key = b64decode('ABEiM0RVZneImQARIjNEVQ==')

    try:

        b64 = json.loads(json_input)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        cipher = AES.new(key, AES.MODE_CFB, iv=iv)
        text = cipher.decrypt(ct)
        print("A MSG é: ", text)

    except (ValueError, KeyError):

        print("Incorrect decryption")
        
    return text

mensagem = (b'oi')

print(criptografar(mensagem))

#descriptografar(mensagemcrpt)


