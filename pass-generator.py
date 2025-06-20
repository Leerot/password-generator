# Password generator

# Specify string length
# Generated a string caracter
# output the string caracter

# import random

import secrets
import string

length = int(input("[*] Specify length of pass: "))

def string_generator(length):
    caracter = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(caracter) for _ in range(length))

print("[+] Password generated: " + string_generator(length))
