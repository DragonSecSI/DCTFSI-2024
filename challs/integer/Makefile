.PHONY: build dist

build:
	gcc chall.c -o chall -O0 -fno-stack-protector -z execstack -no-pie

dist: build
	tar -czvf integer.tar.gz chall chall.c
	cp chall ./app/
