from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

from flask_sqlalchemy import SQLAlchemy

app = Flask( __name__ )

# secret key
app.secret_key = "1k3jg2kl1h21f2g1s12x1fg3xn131"
app.permanent_session_lifetime = timedelta(days = 5)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

# session = {}


# home page
# @app.route("/home")
@app.route("/home")
def home():
    # return "<h1>Hello!</h1> This is the main page."
    # loads an html file
    # return render_template("index.html", content=name)
    return render_template("index.html")


@app.route("/test")
def test():
    return render_template("test.html")


# hello {name} page link
# @app.route("/<name>")
# def user(name):
#    return f"<h1>Hello {name}!</h1>"


# admin redirect
@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin"))


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user_login = request.form["nm"]
        session["user"] = user_login

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()

        flash("Login Successful")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
            flash("Already Logged In!")
        return render_template("login.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email=email)
    else:
        flash("You are not Logged In!")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # if "user" in session:
    #    user = session["user"]
    #    flash(f"You have been logged out!, {user}", "info")
    session.pop("user", None)
    session.pop("email", None)
    flash(f"You have been logged out!", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
