from flask import Flask, redirect, url_for, render_template, request

app = Flask( __name__ )

# secret key
app.secret_key = "1k3jg2kl1h21f2g1s12x1fg3xn131"
session = {}


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
        user_login = request.form["nm"]
        session["user"] = user_login
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
