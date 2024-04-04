# pip install pycryptodome
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

p = getPrime(512)
q = getPrime(512)
n = p * q
e = 3

flag = open("flag.txt", "rb").read()
assert len(flag) == 43

m = bytes_to_long(flag)
c = pow(m, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"ciphertext = {c}")