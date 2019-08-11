from flask import Flask, render_template, request, url_for, redirect, make_response
from models import User, db

app = Flask(__name__)

db.create_all()


@app.route("/", methods=["GET"])
def index():
    page_title = "Acht Ohm - Artist Page"
    return render_template("index.html",
                           page_title=page_title)


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
    return render_template("shop.html",
                           page_title=page_title,
                           page_background=page_background)


@app.route("/contact", methods=["GET"])
def contact():
    page_title = "Acht Ohm - Contact"
    page_background = "/static/img/pexels-photo-2425692.jpeg"
    email_address = request.cookies.get("email")

    if email_address:
        user = db.query(User).filter_by(email=email_address).first()
        user_message = user.message
    else:
        user = None
        user_message = None

    return render_template("contact.html",
                           page_title=page_title,
                           page_background=page_background,
                           user=user,
                           message=user_message)


@app.route("/contact/message", methods=["GET", "POST"])
def message():
    name = request.form.get("user-name")
    email = request.form.get("user-email")
    user_message = request.form.get("user-message")

    # Execption: Cookies im browser gelöscht
    # if email != emails in db:

    user = User(name=name, email=email, message=user_message)

    db.add(user)
    db.commit()

    response = make_response(redirect(url_for("contact")))
    response.set_cookie("email", email)

    # else: Hinweis, dass email bereits in db existiert
    # -->  Springe in if = user Fall bei contact.

    return response

if __name__ == '__main__':
    app.run(debug=True)
