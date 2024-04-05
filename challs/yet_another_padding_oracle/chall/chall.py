# https://pypi.org/project/pycryptodome/
from Crypto.Cipher import AES
import os

key = os.urandom(16)

def pad(message):
    pad_len = 15 - len(message) % 16
    return message + b"\0"*pad_len + bytes([pad_len])

def unpad(message):
    pad_len = message[-1]
    assert sum(message[-pad_len - 1: -1]) == 0
    return message[:-pad_len - 1]

def encrypt(plaintext):
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    padded = pad(plaintext)
    return iv + cipher.encrypt(padded)

def decrypt(ciphertext):
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    padded = cipher.decrypt(ciphertext)
    return unpad(padded)

while True:
    print("What do you want to do?\n1. Encrypt\n2. Encrypt flag\n3. Get flag\n4. Exit")
    choice = input("> ")
    try:
        if choice == "1":
            print("Enter message to encrypt (in hex)")
            plaintext = bytes.fromhex(input("> "))
            print("Ciphertext:", encrypt(plaintext).hex())
        elif choice == "2":
            with open("flag.txt", "rb") as f:
                flag = f.read()
            print("Ciphertext:", encrypt(flag).hex())
        elif choice == "3":
            print("Enter ciphertext to decrypt (in hex)")
            ciphertext = bytes.fromhex(input("> "))
            plaintext = decrypt(ciphertext)
            if plaintext == b"May I kindly have a flag, pretty please?":
                print("Here you go: 🚩")
            else:
                print("Maybe if you ask nicely...")
        elif choice == "4":
            break
        else:
            print("Invalid choice")
            break
    except:
        print("What are you doing, silly?")
