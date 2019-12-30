from flask import Flask, redirect, url_for, render_template, request

app = Flask( __name__ )


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
        return redirect(url_for("user", usr=user_login))
    else:
        return render_template("login.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
