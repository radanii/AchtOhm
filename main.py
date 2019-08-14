import hashlib
import uuid

from flask import Flask, render_template, request, url_for, redirect, make_response
from models import User, db

app = Flask(__name__)

db.create_all()


@app.route("/", methods=["GET"])
def index():
    page_title = "Acht Ohm - Artist Page"

    return render_template("index.html",
                           page_title=page_title)


@app.route("/login", methods=["GET", "POST"])
def login():
    name = request.form.get("user-name")
    email = request.form.get("user-email")
    password = request.form.get("user-password")

    hash_pass = hashlib.sha256(password.encode()).hexdigest()

    user = db.query(User).filter_by(email=email).first()

    if not user:
        user = User(name=name, email=email, message=None, password=hash_pass)

        try:
            db.add(user)
            db.commit()
        except Exception:
            print("Failed to commit db!")
            return "Something went wrong!"

    if hash_pass != user.password:
        return "The entered password seems to be wrong. Please go back and try again!"

    elif hash_pass == user.password:
        session_token = str(uuid.uuid4())

        user.session_token = session_token
        try:
            db.add(user)
            db.commit()
        except Exception:
            print("Failed to commit db!")
            return "Something went wrong!"

        response = make_response(redirect(url_for("shop")))
        response.set_cookie("session_token", session_token, httponly=True, samesite='Strict')

        return response

    return "sucessfully createtd db object!"

@app.route("/tracks", methods=["GET"])
def tracks():
    page_title = "Acht Ohm - Tracks"
    page_background = "/static/img/pexels-photo-2425692.jpeg"
    return render_template("tracks.html",
                           page_title=page_title,
                           page_background=page_background)


@app.route("/shop", methods=["GET"])
def shop():
    page_title = "Acht Ohm - Shop"
    page_background = "/static/img/pexels-photo-2425692.jpeg"
    session_token = request.cookies.get("session_token")

    if session_token:
        user = db.query(User).filter_by(session_token=session_token).first()
    else:
        user = None

    return render_template("shop.html",
                           page_title=page_title,
                           page_background=page_background,
                           user=user)


@app.route("/contact", methods=["GET"])
def contact():
    page_title = "Acht Ohm - Contact"
    page_background = "/static/img/pexels-photo-2425692.jpeg"
    email_address = request.cookies.get("email")

    if email_address:
        user = db.query(User).filter_by(email=email_address).first()
        user_message = user.message
        bool_message = user.bool_message
    else:
        user = None
        user_message = None
        bool_message = "0"

    return render_template("contact.html",
                           page_title=page_title,
                           page_background=page_background,
                           user=user,
                           message=user_message,
                           bool=bool_message)


@app.route("/contact/message", methods=["GET", "POST"])
def message():
    name = request.form.get("user-name")
    email = request.form.get("user-email")
    user_message = request.form.get("user-message")
    bool_message = "1"
    # Execption: Cookies im browser gelöscht
    # if email != emails in db:

    user = db.query(User).filter_by(email=email).first()

    if not user:

        user = User(name=name, email=email, message=user_message, bool_message=bool_message)

        try:
            db.add(user)
            db.commit()
        except Exception:
            print("Failed to commit db!")
            return "Something went wrong!"

        response = make_response(redirect(url_for("contact")))
        response.set_cookie("email", email)

    elif user.bool_message == "1":

        response = make_response(redirect(url_for("contact")))
        response.set_cookie("email", email)

    else:

        user.message = user_message
        user.bool_message = "1"

        try:
            db.add(user)
            db.commit()
        except Exception:
            print("Failed to commit db!")
            return "Something went wrong!"

        response = make_response(redirect(url_for("contact")))
        response.set_cookie("email", email)

    return response


if __name__ == '__main__':
    app.run(debug=True)
