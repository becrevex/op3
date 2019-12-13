#!/usr/bin/env python
# Filename: generate_rsa_keys.py
# This program is optimized for Python 3.4
# Description: Generates RSA keys with 4096 bit length
#   counterpart: None

from Cryptodome.PublicKey import RSA

new_key = RSA.generate(4096)
public_key = new_key.publickey().exportKey("PEM")
private_key = new_key.export_key("PEM")
public_key_file = open("public.pem", "wb")
public_key_file.write(public_key)
public_key_file.close()
private_key_file = open("private.pem", "wb")
private_key_file.write(private_key)
private_key_file.close()
print(public_key.decode())
print(private_key.decode())
