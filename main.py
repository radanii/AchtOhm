from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tracks", methods=["GET"])
def tracks():
    if request.method == "GET":
        return redirect(url_for("tracks"))

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run()