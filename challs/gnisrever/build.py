#!/usr/bin/env python3

import random
import re
import os
import tarfile
from pathlib import Path
from subprocess import Popen

MAGIC = 0xDEAD2BAD
SOURCEFILE = "chall.c"
TEMPFILE = "chall_compile.c"
OUTFILE = "chall"
TARFILE = f"{Path(os.getcwd()).name}.tar.gz"
BUILD_OPTIONS = ["-fstack-protector"]

def main():
    flag = open("flag.txt", encoding="utf-8").read().strip()
    key = random.randbytes(len(flag))

    print("%-20.20s%s" % ("Flag:", flag))
    print("%-20.20s%s" % ("Flag hex:", flag.encode().hex()))
    print("%-20.20s%s" % ("Key:", key.hex()))
    flag_enc = encrypt_flag(pt=flag, key=key)
    print("%-20.20s%s" % ("Encrypted:", flag_enc.hex()))
    flag_dec = decrypt_flag(flag_enc, key)
    print("%-20.20s%s" % ("Decrypted:", flag_dec))
    assert flag == flag_dec

    c_prog = open(SOURCEFILE, encoding="utf-8").read()
    c_prog = re.sub(r'(MAGIC = ).+;', r"\g<1>" + hex(MAGIC) + ";", c_prog, count=1)
    c_prog = re.sub(r'(KEY\[\] = ).+;', r"\g<1>" + to_c_byte_array(key) + ";", c_prog, count=1)
    c_prog = re.sub(r'(FLAG\[\] = ).+;', r"\g<1>" + to_c_byte_array(flag_enc) + ";", c_prog, count=1)
    open(TEMPFILE, "w+", encoding="utf-8").write(c_prog)
    if Popen(["gcc", TEMPFILE, *BUILD_OPTIONS, "-D__PYBUILD__", "-o", OUTFILE]).wait() != 0:
        exit(1)
    os.remove(TEMPFILE)
    with tarfile.open(TARFILE, "w:gz") as tf:
        tf.add(f"{OUTFILE}{'.exe' if os.name == 'nt' else ''}")

def encrypt_flag(pt: str, key: bytes) -> bytes:
    pt = pt.encode("utf-8")
    flag_enc = []

    for i in range(len(pt)):    
        flag_enc.append(((pt[i] ^ key[i]) + MAGIC - i) & 0xFF)

    return bytes(flag_enc)

def decrypt_flag(ct: bytes, key: bytes) -> str:
    flag_dec = []

    for i in range(len(ct)):
        flag_dec.append(((ct[i] - MAGIC + i) & 0xFF) ^ key[i])

    return bytes(flag_dec).decode()

def to_c_byte_array(x: bytes) -> str:
    return "{ 0x" + x.hex(',').replace(',', ', 0x') + " }"

if __name__ == "__main__":
    main()
