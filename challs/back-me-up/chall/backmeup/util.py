import sqlite3
import os
from contextlib import contextmanager
from pathlib import Path
import bcrypt

DATABASE = "/app/database.sqlite3"


@contextmanager
def get_cursor(app):
    conn = sqlite3.connect(DATABASE, check_same_thread=False)
    try:
        yield conn.cursor()
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def hash_password(p: str):
    salt = bcrypt.gensalt(rounds=10, prefix=b"2a")
    return bcrypt.hashpw(p.encode(), salt).decode()


def init(app):
    project_root = Path(__file__).parent.parent
    init_script = project_root / "sql/init.sql"
    sql = init_script.read_text()

    admin_user = f"admin_{os.urandom(24).hex()}"
    admin_password = os.environ["ADMIN_PASSWORD"]
    admin_password = hash_password(admin_password)

    with get_cursor(app) as cursor:
        cursor.executescript(sql)
        cursor.execute("DELETE FROM users WHERE is_admin = 1")
        cursor.execute(
            """INSERT INTO users (username, password, is_admin) VALUES (?, ?, 1)""",
            (admin_user, admin_password),
        )

    # Create the uploads directory
    upload_dir = app.config["UPLOAD_FOLDER"]
    upload_dir.mkdir(parents=True, exist_ok=True)
    # Copy the flag to the uploads directory
    flag = os.environ["FLAG"]
    with (upload_dir / "flag.txt").open("w") as f:
        f.write(flag)
