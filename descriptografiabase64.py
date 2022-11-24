import json

from base64 import b64decode

from Crypto.Cipher import AES

json_input='{"iv":"flu36A9Ai3SdxSL8n+b7Ig==", "ciphertext": "ZV0DgMBd5X/lJYxMeTOBXqU2BQuDQOT7+bHu9H1xoE98"}'

key = b64decode('ABEiM0RVZneImQARIjNEVQ==')

try:

    b64 = json.loads(json_input)
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    text = cipher.decrypt(ct)
    print("A MSG é: ", str(text, 'utf-8'))

except (ValueError, KeyError):

    print("Incorrect decryption")