import random


def key_generator():
    key = random.randint(1, 5)
    return key


def encoder(source_msg, key):
    encrypt_msg = ''
    for current_symbol in source_msg:
        encrypt_msg += chr(ord(current_symbol) + key)

    return encrypt_msg


def decoder(encrypt_msg, key):
    decrypt_msg = ''
    for current_symbol in encrypt_msg:
        decrypt_msg += chr(ord(current_symbol) - key)

    return decrypt_msg
