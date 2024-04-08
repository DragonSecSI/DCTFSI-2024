import base64

flag = open("flag.txt", "rb").read().strip()
flag = base64.b85encode(flag)
flag = bytes(x + 13 for x in flag)[::-1]
print(flag)
