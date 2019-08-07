from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    page_title = "Acht Ohm - Artist Page"
    return render_template("index.html")


@app.route("/tracks")
def tracks():
    page_title = "Acht Ohm - Tracks"
    page_background = "/static/img/pexels-photo-2425692.jpeg"
    return render_template("tracks.html")


@app.route("/shop")
def shop():
    page_title = "Acht Ohm - Shop"
    return render_template("shop.html")


@app.route("/contact")
def contact():
    page_title = "Acht Ohm - Contact"
    return render_template("contact.html")

if __name__ == '__main__':
    app.run()
