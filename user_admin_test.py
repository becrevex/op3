#!/usr/bin/env python
# Filename: user_admin_test.py
# This program is optimized for Python 3.4
# Description: Ctypes call to evaluate user administrator status
#   counterpart: None


import ctypes
if ctypes.windll.shell32.IsUserAnAdmin() == 0:
    print '[-] We are NOT admin! '
else:
    print '[+] We are admin :) '
    
