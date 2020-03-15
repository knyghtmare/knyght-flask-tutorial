from flask import Flask, render_template

from second import second


app = Flask(__name__)
app.register_blueprint(second, url_prefix="/admin")


# define the home page
@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


# test
@app.route("/test")
def test():
    return "This is a Test."


if __name__ == "__main__":
    app.run(debug=True)
