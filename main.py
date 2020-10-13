from flask import Flask, redirect, url_for, render_template, request, session, flash
from forms import RegisterForm, LoginForm
from script import string_validation, integer_validation

app = Flask(__name__)
app.config['SECRET_KEY'] = 'string'


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login_form():
    form = LoginForm()
    if form.is_submitted():
        user = request.form
    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register_form():
    form = RegisterForm()
    if form.is_submitted():
        user_register = request.form
        return redirect(url_for("/success"))
    return render_template("register.html", form=form)


@app.route("/success", methods=["GET", "POST"])
def success():
    return redirect(url_for("/success"))


@app.route("/popplaylist", methods=["GET", "POST"])
def pop_playlist():
    time = integer_validation(0, 10)
    if time > 5:
        return render_template("10pop_playlist.html")
    else:
        return render_template("5pop_playlist.html")


@app.route("/hiphopplaylist", methods=["GET", "POST"])
def hiphop_playlist():
    time = integer_validation(0, 10)
    if time > 5:
        return render_template("10hippop_playlist.html")
    else:
        return render_template("5hippop_playlist.html")


@app.route("/rockplaylist", methods=["GET", "POST"])
def rock_playlist():
    time = integer_validation(0, 10)
    if time > 5:
        return render_template("10rock_playlist.html")
    else:
        return render_template("5rock_playlist.html")


@app.route("/jazzplaylist", methods=["GET", "POST"])
def jazz_playlist():
    time = integer_validation(0, 10)
    if time > 5:
        return render_template("10jazz_playlist.html")
    else:
        return render_template("5jazz_playlist.html")


if __name__ == "__main__":
    app.run()