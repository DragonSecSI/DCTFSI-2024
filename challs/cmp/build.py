from subprocess import Popen
import tarfile
import os
from pathlib import Path

chall = open("chall.c").read()
f = open("chall_compile.c", "w")
f.write("#define FLAG ")
f.write((str([hex(x) for x in open("flag.txt", "rb").read().strip()]).replace("'", "").replace("[", "{").replace("]", "}")))
f.write("\n")
f.write(chall)
f.close()

Popen("gcc -fstack-protector chall_compile.c -o chall".split()).wait()
with tarfile.open(f"{Path(os.getcwd()).name}.tar.gz", "w:gz") as tf:
    tf.add(f"chall{'.exe' if os.name == 'nt' else ''}")
os.remove("chall_compile.c")
