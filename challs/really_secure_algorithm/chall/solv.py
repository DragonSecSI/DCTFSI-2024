from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.PublicKey import RSA
import gmpy2

key = RSA.import_key(open("publickey.pem").read())
e = key.e
n = key.n
c = bytes_to_long(open("ciphertext.bin", "rb").read())

for i in range(2**(43*8*3) // n):
    root = gmpy2.iroot(c + i * n, e)[0]
    flag = long_to_bytes(root)
    if b"dctf{" in flag:
        print(flag)
        break
