from pwn import remote, xor, unhex

io = remote("pwn.dctf.si", 13370)

def oracle(ciphertext):
    io.sendlineafter(b"> ", b"3")
    io.sendlineafter(b"> ", ciphertext.hex())
    if b"nicely" in io.recvline():
        return True
    return False

io.sendlineafter(b"> ", b"2")
enc_flag = unhex(io.recvline().strip().split(b": ")[1])

flag = b""

for i in range(16, len(enc_flag), 16):
    iv = enc_flag[i-16:i]
    block = enc_flag[i:i+16]

    mask = [0xff]*16

    for j in range(16):
        for k in range(256):
            mask[-j - 1] = k
            if oracle(xor(iv, mask) + block):
                break
        else:
            print("Failed")
            exit()
        mask[-1] ^= j ^ (j+1)

    flag += xor(mask, [0]*15 + [16])
    print(flag)
