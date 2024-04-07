import os

def xor(data, key):
    ciphertext = []
    for i in range(len(data)):
        ciphertext.append(data[i] ^ key[i % len(key)])
    return bytes(ciphertext)

with open("./flag.txt", "rb") as f:
    flag = f.read()

assert len(flag) == 56

key = os.urandom(100) # 100 random bytes

plaintext = b"Hey! You! Yes, you there! I have a secret to tell you! Please don't share it with anyone else! The flag is: "
plaintext += flag

with open("./ciphertext.txt", "wb") as f:
    f.write(xor(plaintext, key))
