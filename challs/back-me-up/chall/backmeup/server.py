from flask import (
    Flask,
    flash,
    render_template,
    request,
    redirect,
    url_for,
    send_file,
    session,
)
import sqlite3
from werkzeug.utils import secure_filename
import bcrypt, os
from backmeup.util import get_cursor, hash_password

app = Flask(__name__)

ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}


def allowed_file(filename):
    if "flag.txt" in filename:
        # Doing something sussy :D
        return False
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part.")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file.")
            return redirect(request.url)
        if not file or not file.filename or not allowed_file(file.filename):
            flash("Invalid file.")
            return render_template("upload.html")
        filename = secure_filename(file.filename)
        save_path = app.config["UPLOAD_FOLDER"] / filename
        if save_path.exists():
            flash("File already exists")
            return render_template("upload.html")
        # Check size less than 5MB
        if file.seek(0, os.SEEK_END) > 5 * 1024 * 1024:
            flash("File too large. Max size is 5MB.")
            return render_template("upload.html")
        file.save(save_path)
        return render_template(
            "upload.html",
            message=f"File uploaded successfully to {save_path.as_posix()}",
            link=f"/uploads{filename}",
        )

    return render_template("upload.html", message="Upload a file")


@app.route("/uploads/<path:filename>", methods=["GET"])
def uploaded_file(filename: str):
    finalpath: str = (app.config["UPLOAD_FOLDER"] / filename).resolve().as_posix()
    if not finalpath.startswith("/app/data"):  # Prevent path traversal
        return "Invalid path", 403
    if "flag.txt" in finalpath and session.get("admin") != 1:
        return "Invalid path", 403
    return send_file(finalpath, as_attachment=False)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        with get_cursor(app) as cursor:
            user = cursor.execute(
                "SELECT username, password, is_admin FROM users WHERE username = ?",
                (username,),
            ).fetchone()
        if user and bcrypt.checkpw(password.encode(), user[1].encode()):
            # Login successful
            session["admin"] = user[2]
            return redirect(url_for("index"))
        else:
            # Login failed
            flash("Invalid username or password")
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_password = hash_password(password)
        try:
            with get_cursor(app) as cursor:
                cursor.execute(
                    "INSERT INTO users (username, password, is_admin) VALUES (?, ?, 0)",
                    (username, hashed_password),
                )
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Username already exists")
    return render_template("register.html")
