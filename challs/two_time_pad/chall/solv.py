def xor(data, key):
    ciphertext = []
    for i in range(len(data)):
        ciphertext.append(data[i] ^ key[i % len(key)])
    return bytes(ciphertext)

with open("./ciphertext.txt", "rb") as f:
    ciphertext = f.read()

known = b"Hey! You! Yes, you there! I have a secret to tell you! Please don't share it with anyone else! The flag is: "

key = xor(known, ciphertext)[:100]

plaintext = xor(ciphertext, key)

print(plaintext)
