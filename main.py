from flask import Flask, render_template


app = Flask(__name__)


# define the home page
@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
