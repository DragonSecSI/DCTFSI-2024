# https://pypi.org/project/pycryptodome/
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.PublicKey import RSA

key = RSA.generate(1024, e=3)
with open("publickey.pem", "wb") as f:
    f.write(key.public_key().export_key())

n = key.n
e = key.e

flag = open("flag.txt", "rb").read()
assert len(flag) == 43

m = bytes_to_long(flag)
c = pow(m, e, n)

with open("ciphertext.bin", "wb") as f:
    f.write(long_to_bytes(c))
