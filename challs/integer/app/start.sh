#!/bin/bash
chown pilot:pilot /app/chall
chmod +x /app/chall
while true; do
	su pilot -c 'timeout -k 30 1d socat TCP-LISTEN:5555,nodelay,reuseaddr,fork EXEC:"stdbuf -i0 -o0 -e0 ./baby_bof"'
done
