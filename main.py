from flask import Flask, redirect, url_for, render_template, request, session
from forms import RegisterForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'string'


@app.route("/", methods=["GET", "POST"])
def homepage():
    return render_template("base.html")


@app.route("/login", methods=["POST", "GET"])
def login_form():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("/listennow"))
    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register_form():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for("/sucess"))
    return render_template("register.html", form=form)


@app.route("/success", methods=["GET", "POST"])
def success():
    return render_template("success.html")


@app.route("/playlists", methods=["GET", "POST"])
def playlist():
    return render_template("playlists.html")


if __name__ == "__main__":
    app.run()