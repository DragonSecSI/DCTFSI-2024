from Crypto.Util.number import long_to_bytes
import gmpy2

output = open("./output.txt", "r").read().split("\n")

n = int(output[0].split(" = ")[1])
e = int(output[1].split(" = ")[1])
c = int(output[2].split(" = ")[1])

for i in range(2**(43*8) // n):
    root = gmpy2.iroot(c + i * n, e)[0]
    flag = long_to_bytes(root)
    if b"dctf{" in flag:
        print(flag)
        break
