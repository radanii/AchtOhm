from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route("/")
def index():
    page_title = "Acht Ohm - Artist Page"
    return render_template("index.html",
                           page_title=page_title)


@app.route("/tracks")
def tracks():
    page_title = "Acht Ohm - Tracks"
    page_background = "/static/img/pexels-photo-2425692.jpeg"
    return render_template("tracks.html",
                           page_title=page_title,
                           page_background=page_background)


@app.route("/shop")
def shop():
    page_title = "Acht Ohm - Shop"
    page_background = "/static/img/pexels-photo-2425692.jpeg"
    return render_template("shop.html",
                           page_title=page_title,
                           page_background=page_background)


@app.route("/contact")
def contact():
    page_title = "Acht Ohm - Contact"
    page_background = "/static/img/pexels-photo-2425692.jpeg"
    return render_template("contact.html",
                           page_title=page_title,
                           page_background=page_background)


if __name__ == '__main__':
    app.run(debug=True)
