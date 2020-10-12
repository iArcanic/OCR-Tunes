from flask import Flask, redirect, url_for, render_template, request, session, flash
from forms import RegisterForm, LoginForm
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'string'
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#
# db = SQLAlchemy(app)
#
#
# class users(db.Model):
#     _id = db.Column(db.Integer, primary_key="True")
#     first_name = db.Column(db.String(100))
#     last_name = db.Column(db.String(100))
#     username = db.Column(db.String(100))
#     password = db.Column(db.String(100))
#     genre = db.Column(db.String(100))
#     favourite_artist = db.Column(db.String(100))
#     birthday = db.Column(db.String(100))
#
#     def __init__(self, first_name, last_name, username, password, genre, favourite_artist, birthday):
#         self.first_name = first_name
#         self.last_name = last_name


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login_form():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("/playlists"))
    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register_form():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        return redirect(url_for("/success"))
    return render_template("register.html", form=form)


@app.route("/success", methods=["GET", "POST"])
def success():
    return redirect(url_for("/success"))


@app.route("/playlists", methods=["GET", "POST"])
def playlist():
    return render_template("playlists.html")


if __name__ == "__main__":
    # db.create_all()
    app.run()