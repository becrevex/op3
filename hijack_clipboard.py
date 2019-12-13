#!/usr/bin/env python
# Filename: hijack_clipboard.py
# This program is optimized for Python 3.4
# Description: Code to copy the contents of the system clipboard and print results
#   counterpart: None

import time
try:
    import pyperclip
except:
    command = "pip3 install pyperclip"
    CMD = subprocess.Popen(command,
                       shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       stdin=subprocess.PIPE)
 
list = [] 
while True:
    if pyperclip.paste() != 'None':
        value = pyperclip.paste() 
        if value not in list:
            list.append(value)
        print(list)
        time.sleep(3)
