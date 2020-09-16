def make_pair_key(e, d, module):
    public_key = (e, module)
    print('\n\nYour public key: ' + str(public_key))
    closed_key = (d, module)
    file = open('./cs.txt', 'w')
    check = file.write(str(closed_key))

    if check == 0:
        print('Your closed key not writed to file.\nReload script')
    print('Your closed key writed to file "cs.txt"')


def encrypt_message(e, module):
    source_message = input('\nEnter message for encrypt: ')
    encrypt_message = []
    encrypt_str = ''
    for i in source_message:
        encrypt_message.append((ord(i) ** e) % module)
    for i in encrypt_message:
        encrypt_str += chr(i)
    print('\nEncryption message: ' + encrypt_str)
    return encrypt_message


def decrypt_message(encrypt_message, d, module):
    decrypt_message = []
    decrypt_str = ''
    for i in encrypt_message:
        decrypt_message.append((i ** d) % module)
    for i in decrypt_message:
        decrypt_str += chr(i)

    return decrypt_str


p = 17
q = 19
module = p * q
function_euler = (p - 1) * (q - 1)
e = 5
d = 173

make_pair_key(e, d, module)
enc = encrypt_message(e, module)
dec = decrypt_message(enc, d, module)
print('Decryption message: ' + dec + '\n\n')
